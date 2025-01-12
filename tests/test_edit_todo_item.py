from playwright.sync_api import Playwright, sync_playwright, expect
from pom.todo_elements import Elements


def test_edit_todo_item(set_up) -> None:
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
    page.get_by_role("button").nth(2).click()
    page.get_by_label("Title").click()
    page.get_by_label("Title").fill("Holiday Plan")
    page.get_by_role("button", name="Update Task").click()
    expect(elements.holiday_plan, "Error while editing the item into new 'Holiday Plan'").to_be_visible()
    print(f"Previous item of 'Groceries' has been successfully changed into 'Holiday Plan' in to-do list ")

    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    test_edit_todo_item(playwright)
