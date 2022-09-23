import pytest
import selenium.webdriver as webdriver
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage

from pageObjects.ConfirmPage import ConfirmPage

# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("Getting all the card titles!!!!!")
        # checkoutPage = CheckoutPage(self.driver)   # moved to HomePage
        cards = checkoutPage.getCardsTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            # log.info(cardText)
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()


        confirmPage = checkoutPage.checkoutItems()
        # confirmpage = checkoutpage.checkOutItems()
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        # confirmPage = ConfirmPage(self.driver)
        confirmPage.checkout().click()
        # log.info("Entering country name as ind")
        log.info('Entering country name as ind')
        # self.driver.find_element(By.ID, "country").send_keys("ind")
        confirmPage.search_country().send_keys("ind")
        # time.sleep(5)
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located(confirmPage.india))   # Moved to baseclass
        self.verifyLinkPresent(confirmPage.india)
        confirmPage.India().click()
        confirmPage.checkbox().click()
        confirmPage.purchase_button().click()
        textMatch = confirmPage.success_alert().text
        log.info("Text received from application is "+textMatch)

        assert ("Success! Thank you!" in textMatch)


