import asyncio
from playwright.async_api import async_playwright

async def scrape_linkedin():
    url = "https://www.linkedin.com/in/mikemalburg"
    login_wait_time = 60
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = await context.new_page()
        
        print(f"Navigating to {url}")
        print(f"WARNING: You have {login_wait_time} seconds to log in manually if needed!")
        await page.goto(url, wait_until="networkidle")
        
        # Check if on login page
        if "signin" in page.url:
            print("Hit login page. You have 60 seconds to log in...")
            await asyncio.sleep(login_wait_time)
            await page.goto(url, wait_until="networkidle")
        
        # Wait for profile
        await page.wait_for_selector("body", timeout=15000)
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(2)
        
        # Save content
        content = await page.content()
        with open("linkedin_profile.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Saved HTML")
        
        text_content = await page.evaluate("() => document.body.innerText")
        with open("linkedin_profile.txt", "w", encoding="utf-8") as f:
            f.write(text_content)
        print("Saved text")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_linkedin())
