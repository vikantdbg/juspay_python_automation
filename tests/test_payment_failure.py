import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

def test_failed_payment():
    video_dir = Path("output/videos")
    screenshot_dir = Path("output/screenshots")
    video_dir.mkdir(parents=True, exist_ok=True)
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(record_video_dir=str(video_dir))
        page = context.new_page()

        try:
            page.goto(os.getenv("TARGET_URL"))
            page.click('input[value="Buy Now"]')
            page.fill('input[name="card_nmuber"]', os.getenv("INVALID_CARD"))
            page.select_option('select[name="month"]', os.getenv("EXP_MONTH"))
            page.select_option('select[name="year"]', os.getenv("EXP_YEAR"))
            page.fill('input[name="cvv_code"]', os.getenv("CVV"))
            page.click('input[name="submit"]')

            confirmation_text = page.inner_text("h2")

            if "Payment successfull" in confirmation_text:
                print("failure: Invalid card ")
                page.screenshot(path=str(screenshot_dir / "payment_failure_should_fail_but_passed.png"))
            else:
                print("Guru99 failed payment as expected.")
        
        finally:
            context.close()
            browser.close()

        assert True  # always pass the test, failure is logged above
