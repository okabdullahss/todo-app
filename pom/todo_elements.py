
class Elements:
    def __init__(self, page):

        self.groceries = page.get_by_text("Groceries")
        self.bills = page.get_by_text("Bills")
        self.winter_tires = page.get_by_text("Winter Car Tires")
        self.holiday_plan = page.get_by_text("Holiday Plan")
        self.strikeout_element = page.locator("p[class*='todoText--completed']")
        self.deleted_pop_up = page.locator("div[role='status']").nth(0)