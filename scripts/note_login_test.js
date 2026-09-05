require('dotenv').config();
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', headless: true });
  const page = await browser.newPage();
  try {
    await page.goto('https://note.com/login', { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.screenshot({ path: '/tmp/note_login_page.png' });

    const emailInput = page.locator('input[name="login"], input[type="email"], input[type="text"]').first();
    await emailInput.waitFor({ timeout: 15000 });
    await emailInput.fill(process.env.NOTE_ID);

    const passInput = page.locator('input[type="password"]').first();
    await passInput.fill(process.env.NOTE_PASSWORD);

    await page.screenshot({ path: '/tmp/note_login_filled.png' });

    const submitButton = page.locator('button[type="submit"]').first();
    await submitButton.click();

    await page.waitForTimeout(5000);
    await page.screenshot({ path: '/tmp/note_login_result.png' });

    console.log('CURRENT_URL:', page.url());
  } catch (err) {
    console.error('ERROR:', err.message);
    await page.screenshot({ path: '/tmp/note_login_error.png' }).catch(() => {});
  } finally {
    await browser.close();
  }
})();
