import pytest
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        # homePage.inputName().send_keys(getData[0]) # when parameters stored as tuple
        log.info("First name is "+getData["first_name"])
        homePage.inputName().send_keys(getData["first_name"])  # when the parameters are stored as dictionary
        # homePage.inputEmail().send_keys(getData[1]) #when parameters stored as tuple
        homePage.inputEmail().send_keys(getData["email"])  # when the parameters are stored as dictionary
        homePage.checkButton().click()
        # self.selectOptionByText(homePage.getGender(), getData[2]) # when parameters stored as tuple
        self.selectOptionByText(homePage.getGender(), getData["gender"])  # when the parameters are stored as dictionary
        homePage.selectStudentAsEmplStatus().click()
        homePage.submit().click()
        message = homePage.success_alert().text
        print(message)
        assert 'Success' in message
        self.driver.refresh()

    # Data sets can be passed as tuple.
    # @pytest.fixture(params=[("Shwetha", "Amogh@123.com", "Female"), ("Amogh", "Nagaraj@123.com", "Male")])
    # def getData(self, request):
    #    return request.param

    # Data Sets can also be passed as dictionary.
    # @pytest.fixture(params=[{"first_name": "Shwetha", "email": "Amogh@123.com", "gender": "Female"},
    #                         {"first_name": "Amogh", "email": "Nagaraj@123.com", "gender": "Male"}])
    # def getData(self, request):
    #     return request.param

    # Created a new folder for testdata. all the test data related to this test case moved to HomePageData.py class.

    @pytest.fixture(params=HomePageData.test_Homepage_Data)
    def getData(self, request):
        return request.param

