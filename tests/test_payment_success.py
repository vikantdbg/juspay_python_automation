import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

def test_successful_payment():
    output_dir = Path("output/videos")
    output_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            record_video_dir=str(output_dir)
        )
        page = context.new_page()
        try:
            page.goto(os.getenv("TARGET_URL"))
            page.click('input[value="Buy Now"]')
            page.fill('input[name="card_nmuber"]', os.getenv("VALID_CARD"))
            page.select_option('select[name="month"]', os.getenv("EXP_MONTH"))
            page.select_option('select[name="year"]', os.getenv("EXP_YEAR"))
            page.fill('input[name="cvv_code"]', os.getenv("CVV"))
            page.click('input[name="submit"]')

            assert "Payment successfull" in page.inner_text("h2")

        except Exception as e:
            Path("output/screenshots").mkdir(parents=True, exist_ok=True)
            page.screenshot(path="output/screenshots/payment_success_failed.png")
            raise e

        finally:
            context.close()
            browser.close()
