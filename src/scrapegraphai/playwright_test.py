
async def ascrape_playwright(url: str) -> str:
    """
    Asynchronously scrape the content of a given URL using Playwright's async API.

    Args:
        url (str): The URL to scrape.

    Returns:
        str: The scraped HTML content or an error message if an exception occurs.

    """
    from playwright.async_api import async_playwright
    from undetected_playwright import Malenia

    print("Starting scraping...")
    results = ""
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True, proxy=None
        )
        try:
            context = await browser.new_context()
            await Malenia.apply_stealth(context)
            page = await context.new_page()
            await page.goto(url)
            await page.wait_for_load_state(self.load_state)
            results = await page.content()  # Simply get the HTML content
            print("Content scraped")
        except Exception as e:
            results = f"Error: {e}"
        await browser.close()
    return results

if __name__ == '__main__':
    ascrape_playwright()
