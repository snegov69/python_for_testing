# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAuthorisation(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path=r'/Users/v.bushlanov')
        self.wd.implicitly_wait(30)

    def test_authorisation(self):
        wd = self.wd
        wd.get("https://qa.price-port.ru/")
        wd.find_element_by_css_selector("a.button.button_accent.button-icon.header__button-personal > svg > path").click()
        wd.get("https://partner.qa.price-port.ru/sign-in")
        wd.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div/form/div/div/label").click()
        wd.find_element_by_id(":R1svf9tkq:-form-item").clear()
        wd.find_element_by_id(":R1svf9tkq:-form-item").send_keys("v.bushlanov@thehead.ru")
        wd.find_element_by_xpath("//button[@type='submit']").click()
        wd.get("https://partner.qa.price-port.ru/")
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()


#     python3.12 -m venv /Users/v.bushlanov//Users/v.bushlanov/Documents/GitHub/python_for_testing
#     source /Users/v.bushlanov/Python/bin/activate
#     python3.12 -m pip install requests