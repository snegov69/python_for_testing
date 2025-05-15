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
        self.driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_authorisation(self):
        driver = self.driver
        driver.get("https://qa.price-port.ru/")
        driver.find_element_by_css_selector("a.button.button_accent.button-icon.header__button-personal > svg > path").click()
        driver.get("https://partner.qa.price-port.ru/sign-in")
        driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div/form/div/div/label").click()
        driver.find_element_by_id(":R1svf9tkq:-form-item").clear()
        driver.find_element_by_id(":R1svf9tkq:-form-item").send_keys("v.bushlanov@thehead.ru")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.get("https://partner.qa.price-port.ru/")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
