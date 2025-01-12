from playwright.sync_api import Playwright, sync_playwright, expect


def test_addItem(set_up) -> None:
    page = set_up
    page.goto("https://wc-react-todo-app.netlify.app/")
    page.get_by_role("button", name="Add Task").click()
    page.get_by_label("Title").click()
    page.get_by_label("Title").fill("Groceries")
    page.locator("form").get_by_role("button", name="Add Task").click()
    expect(set_up.elements.groceries, "Error while adding the item 'Groceries' to the list").to_be_visible()
    print(f"Item 'Groceries' has been successfully add into to-do list")

    # ---------------------


with sync_playwright() as playwright:
    test_addItem(playwright)
