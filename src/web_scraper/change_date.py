from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select

from web_scraper.popup import close_popup


class DateChanger:
    def __init__(self, driver):

        self.driver = driver

    def change_date(self, desired_dates):
        close_popup(self.driver)

        all_dates = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(
                (
                    By.XPATH,
                    "//select[contains(@class, 'dropdown-select ng-untouched ng-pristine ng-valid')]",
                )
            )
        )
        for i, date_elem in enumerate(all_dates):
            select = Select(date_elem)
            if i % 2 == 0:
                select.select_by_value(desired_dates[i])
            else:
                select.select_by_visible_text(desired_dates[i])

        submit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//i[contains(@class, 'icon icon--submit')]")
            )
        )
        submit.click()
