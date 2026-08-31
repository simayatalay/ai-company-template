from playwright.sync_api import sync_playwright


def run_browser_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("http://localhost:8000")

        page.fill("#nameInput", "Simay")
        page.click("#greetButton")

        result = page.text_content("#result")

        expected = "Hello, Simay! Welcome to the project."

        if result == expected:
            print("Browser Test Result: PASS")
        else:
            print("Browser Test Result: FAIL")
            print(f"Expected: {expected}")
            print(f"Actual: {result}")

        browser.close()


if __name__ == "__main__":
    run_browser_test()