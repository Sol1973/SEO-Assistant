/**
 * AUDIT CONTROLLER
 * Business logic for SEO audits
 */

const puppeteer = require('puppeteer');
const cheerio = require('cheerio');
const { run, get } = require('../models/database');

/**
 * Start a new SEO audit
 */
const startAudit = async (url) => {
  try {
    // Create audit record
    const result = await run(
      'INSERT INTO audits (url, status) VALUES (?, ?)',
      [url, 'pending']
    );

    // Start audit in background (simplified for MVP)
    processAudit(result.id, url);

    return {
      success: true,
      data: {
        auditId: result.id,
        url,
        status: 'pending'
      }
    };
  } catch (error) {
    throw new Error(`Error starting audit: ${error.message}`);
  }
};

/**
 * Process audit (background task)
 */
const processAudit = async (auditId, url) => {
  try {
    // Launch browser
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle2' });

    // Get page content
    const html = await page.content();
    const $ = cheerio.load(html);

    // Analyze meta tags
    const metaScore = analyzeMetaTags($);

    // Analyze headings
    const headingsScore = analyzeHeadings($);

    // Analyze images
    const imagesScore = analyzeImages($);

    // Calculate overall score
    const overallScore = Math.round((metaScore + headingsScore + imagesScore) / 3);

    // Save results
    const results = JSON.stringify({
      metaTags: { score: metaScore },
      headings: { score: headingsScore },
      images: { score: imagesScore }
    });

    await run(
      `UPDATE audits 
       SET status = ?, completed_at = CURRENT_TIMESTAMP, 
           meta_score = ?, headings_score = ?, images_score = ?, 
           overall_score = ?, results = ?
       WHERE id = ?`,
      ['completed', metaScore, headingsScore, imagesScore, overallScore, results, auditId]
    );

    await browser.close();
    console.log(`✅ Audit ${auditId} completed`);
  } catch (error) {
    console.error(`❌ Error processing audit ${auditId}:`, error.message);
    await run('UPDATE audits SET status = ? WHERE id = ?', ['failed', auditId]);
  }
};

/**
 * Analyze meta tags
 */
const analyzeMetaTags = ($) => {
  let score = 0;
  const checks = [];

  // Title
  const title = $('title').text();
  if (title && title.length >= 30 && title.length <= 60) {
    score += 25;
    checks.push('✅ Title length optimal');
  } else {
    checks.push('❌ Title length not optimal');
  }

  // Description
  const description = $('meta[name="description"]').attr('content');
  if (description && description.length >= 120 && description.length <= 160) {
    score += 25;
    checks.push('✅ Description length optimal');
  } else {
    checks.push('❌ Description length not optimal');
  }

  // Canonical
  if ($('link[rel="canonical"]').length > 0) {
    score += 25;
    checks.push('✅ Canonical URL present');
  } else {
    checks.push('❌ Canonical URL missing');
  }

  // Open Graph
  if ($('meta[property^="og:"]').length >= 3) {
    score += 25;
    checks.push('✅ Open Graph tags present');
  } else {
    checks.push('❌ Open Graph tags missing');
  }

  return score;
};

/**
 * Analyze headings structure
 */
const analyzeHeadings = ($) => {
  let score = 0;
  const checks = [];

  // H1
  const h1Count = $('h1').length;
  if (h1Count === 1) {
    score += 40;
    checks.push('✅ Single H1 found');
  } else if (h1Count === 0) {
    checks.push('❌ No H1 found');
  } else {
    checks.push(`⚠️ Multiple H1 tags (${h1Count})`);
    score += 20;
  }

  // H2-H6 hierarchy
  const h2Count = $('h2').length;
  const h3Count = $('h3').length;

  if (h2Count > 0) {
    score += 30;
    checks.push(`✅ ${h2Count} H2 tags found`);
  }

  if (h3Count > 0) {
    score += 30;
    checks.push(`✅ ${h3Count} H3 tags found`);
  } else if (h2Count === 0 && h3Count === 0) {
    checks.push('❌ No heading hierarchy');
  }

  return Math.min(score, 100);
};

/**
 * Analyze images
 */
const analyzeImages = ($) => {
  let score = 0;
  const images = $('img');
  const totalImages = images.length;

  if (totalImages === 0) {
    return 100; // No images = no issues
  }

  let imagesWithAlt = 0;
  let imagesWithOptimalAlt = 0;

  images.each((i, img) => {
    const alt = $(img).attr('alt');
    if (alt) {
      imagesWithAlt++;
      if (alt.length >= 5 && alt.length <= 125) {
        imagesWithOptimalAlt++;
      }
    }
  });

  // Alt text present
  const altPercentage = (imagesWithAlt / totalImages) * 100;
  if (altPercentage >= 90) {
    score += 50;
  } else if (altPercentage >= 70) {
    score += 35;
  } else if (altPercentage >= 50) {
    score += 20;
  }

  // Alt text optimal
  const optimalPercentage = (imagesWithOptimalAlt / totalImages) * 100;
  if (optimalPercentage >= 80) {
    score += 50;
  } else if (optimalPercentage >= 60) {
    score += 35;
  } else if (optimalPercentage >= 40) {
    score += 20;
  }

  return Math.min(score, 100);
};

/**
 * Get audit results
 */
const getAuditResults = async (auditId) => {
  try {
    const audit = await get('SELECT * FROM audits WHERE id = ?', [auditId]);

    if (!audit) {
      throw new Error('Audit not found');
    }

    return {
      success: true,
      data: {
        auditId: audit.id,
        url: audit.url,
        status: audit.status,
        results: audit.results ? JSON.parse(audit.results) : null,
        overallScore: audit.overall_score,
        createdAt: audit.created_at,
        completedAt: audit.completed_at
      }
    };
  } catch (error) {
    throw new Error(`Error getting audit results: ${error.message}`);
  }
};

module.exports = {
  startAudit,
  getAuditResults
};

