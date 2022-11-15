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
        log.info("Getting all the card titles!!")
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
        confirmPage.checkout().click()
        log.info('Entering country name as ind')
        confirmPage.search_country().send_keys("ind")
        self.verifyLinkPresent(confirmPage.india)
        confirmPage.India().click()
        confirmPage.checkbox().click()
        confirmPage.purchase_button().click()
        textMatch = confirmPage.success_alert().text
        log.info("Text received from application is "+textMatch)

        assert ("Success! Thank you!" in textMatch)


