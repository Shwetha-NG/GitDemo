from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    # cards = self.driver.find_elements(By.CSS_SELECTOR, '.card-title a')
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.XPATH, "(//button[@class='btn btn-info'])")
    checkout_item = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getCardsTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    # * should be written to deserialize the tuple

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.card_footer)

    def checkoutItems(self):
        self.driver.find_element(*CheckoutPage.checkout_item).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
