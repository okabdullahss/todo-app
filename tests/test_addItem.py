from playwright.sync_api import Playwright, sync_playwright, expect
from pom.todo_elements import Elements

def test_addItem(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    elements = Elements(page)
    page.goto("https://wc-react-todo-app.netlify.app/")
    page.get_by_role("button", name="Add Task").click()
    page.get_by_label("Title").click()
    page.get_by_label("Title").fill("Groceries")
    page.locator("form").get_by_role("button", name="Add Task").click()
    expect(elements.groceries, "Error while adding the item 'Groceries' to the list").to_be_visible()
    print(f"Item 'Groceries' has been successfully add into to-do list")

    # ---------------------
    context.close()
    browser.close()
