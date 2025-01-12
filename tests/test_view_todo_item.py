from playwright.sync_api import Playwright, sync_playwright, expect
from pom.todo_elements import Elements


def test_view_todo_items(set_up) -> None:
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page = set_up
    elements = Elements(page)

    page.goto("https://wc-react-todo-app.netlify.app/")
    page.get_by_role("button", name="Add Task").click()
    page.get_by_label("Title").click()
    page.get_by_label("Title").fill("Bills")
    page.locator("[type=submit]").click()
    page.wait_for_timeout(500)

    page.get_by_role("button", name="Add Task").click()
    page.get_by_label("Title").click()
    page.get_by_label("Title").fill("Winter Car Tires")
    page.locator("[type=submit]").click()
    page.wait_for_timeout(500)

    page.get_by_role("button", name="Add Task").click()
    page.get_by_label("Title").click()
    page.get_by_label("Title").fill("Groceries")
    page.locator("[type=submit]").click()
    page.wait_for_timeout(500)

    expect(elements.bills, "Error while adding the item 'Bills' to the list").to_be_visible()
    expect(elements.winter_tires,
           "Error while adding the item 'Winter Car Tires' to the list").to_be_visible()
    expect(elements.groceries, "Error while adding the item 'Groceries' to the list").to_be_visible()
    print(f"All items on the to-do list are successfully viewed ")

    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    test_view_todo_items(playwright)
