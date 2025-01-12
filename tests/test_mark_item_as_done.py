from playwright.sync_api import Playwright, sync_playwright, expect
from pom.todo_elements import Elements


def test_mark_item_as_done(set_up) -> None:
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page = set_up
    elements = Elements(page)

    page.goto("https://wc-react-todo-app.netlify.app/")
    page.get_by_role("button", name="Add Task").click()
    page.get_by_label("Title").click()
    page.get_by_label("Title").fill("Groceries")
    page.locator("[type=submit]").click()
    page.wait_for_timeout(500)
    page.get_by_role("img").first.click()
    page.wait_for_timeout(1000)
    expect(elements.strikeout_element, "Error while marking the item 'Groceries' ").to_be_visible()
    print(f"Item 'Groceries' has been successfully marked as done")

    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    test_mark_item_as_done(playwright)
