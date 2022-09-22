from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
    country_search = (By.ID, "country")
    india = (By.LINK_TEXT, "India")
    check_box = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_btn = (By.CSS_SELECTOR, "[type='submit']")
    success_alrt = (By.CSS_SELECTOR, "[class*='alert-success']")

    def checkout(self):
        return self.driver.find_element(*ConfirmPage.checkout_button)

    def search_country(self):
        return self.driver.find_element(*ConfirmPage.country_search)

    def India(self):
        return self.driver.find_element(*ConfirmPage.india)

    def checkbox(self):
        return self.driver.find_element(*ConfirmPage.check_box)

    def purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchase_btn)

    def success_alert(self):
        return self.driver.find_element(*ConfirmPage.success_alrt)
