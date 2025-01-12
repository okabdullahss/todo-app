from playwright.sync_api import Playwright, sync_playwright, expect
from pom.todo_elements import Elements


def test_delete_todo_item(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    elements = Elements(page)

    page.goto("https://wc-react-todo-app.netlify.app/")
    page.get_by_role("button", name="Add Task").click()
    page.get_by_label("Title").click()
    page.get_by_label("Title").fill("Groceries")
    page.locator("[type=submit]").click()
    page.wait_for_timeout(500)
    page.get_by_role("button").nth(1).click()
    expect(elements.deleted_pop_up, "Error while deleting the item 'Groceries' ").to_be_visible()
    print(f"Item 'Groceries' has been successfully removed from the to-do list")

    # ---------------------
    context.close()
    browser.close()



