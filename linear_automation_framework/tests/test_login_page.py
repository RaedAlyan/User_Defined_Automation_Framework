import time
import linear_automation_framework.configurations.testData as TestData
from linear_automation_framework.pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TestLoginPage:

    def test_login(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(TestData.sign_in_page)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 30).until(
            ec.visibility_of_element_located((By.ID, 'email'))
        ).send_keys(TestData.email)
        WebDriverWait(self.driver, 30).until(
            ec.visibility_of_element_located((By.ID, 'pass'))
        ).send_keys(TestData.password)
        WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, '//button[@name="send" and @id="send2"]'))
        ).click()
        time.sleep(2)
        title = self.driver.title
        assert title == 'My Account',  "Login Not Successful"
