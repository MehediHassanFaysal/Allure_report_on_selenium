import time

from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By

@allure.severity(allure.severity_level.NORMAL)                    # declare this in class level or method level
class TestNopCommerce:

    @allure.severity(allure.severity_level.MINOR)
    def test_admin_area_demo(self):
        self.driver=webdriver.Chrome()            # here, chromedriver initially declared in the python/Scripts
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        status = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Admin area demo']").is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    @allure.severity(allure.severity_level.NORMAL)
    def test_userlist(self):
        pytest.skip("Skipping test ..Later I will implement..")

    @allure.severity(allure.severity_level.CRITICAL)                   # BLOCKER
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        email = self.driver.find_element(By.ID, "Email")
        email.clear()
        email.send_keys("admin@yourstore.com")
        password = self.driver.find_element(By.ID, "Password")
        password.clear()
        password.send_keys("admin")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()

        time.sleep(3)

        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration 123123":
            self.driver.quit()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name = "testLoginScreen", attachment_type=AttachmentType.PNG)    # capture failure points screenshot
            self.driver.quit()
            assert False


