from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    check_button = (By.ID, "exampleCheck1")
    employment_status = (By.XPATH, "//input[@value='option1']")
    submit_button = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")
    gender_dropdown = (By.ID, "exampleFormControlSelect1")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def inputName(self):
        return self.driver.find_element(*HomePage.name)

    def inputEmail(self):
        return self.driver.find_element(*HomePage.email)

    def checkButton(self):
        return self.driver.find_element(*HomePage.check_button)

    def selectStudentAsEmplStatus(self):
        return self.driver.find_element(*HomePage.employment_status)

    def submit(self):
        return self.driver.find_element(*HomePage.submit_button)

    def success_alert(self):
        return self.driver.find_element(*HomePage.alert)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender_dropdown)
