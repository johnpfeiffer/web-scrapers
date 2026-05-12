import argparse
from playwright.sync_api import sync_playwright

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL to scrape")
    args = parser.parse_args()
    get_answer(args.url)
    print("done")


def get_answer(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded")

        # page/content specific areas to extract
        article = page.locator("article")
        question = article.locator("h1").inner_text()
        print(question.strip())

        page.get_by_role("button", name="Reveal Answer").click()

        # DEBUG: print(page.get_by_text("The Answer").count())
        # climb to the nearest ancestor div that contains a paragraph
        answer = (page.get_by_text("The Answer", exact=True).locator("xpath=ancestor::div[.//p][1]/p").inner_text())
        print(answer.strip())

        browser.close()


if __name__ == "__main__":
    main()

