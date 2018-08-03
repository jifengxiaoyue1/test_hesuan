# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Denglu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://59.110.227.225:8081/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_denglu(self):
        driver = self.driver
        driver.get(self.base_url + "/aplus_ote_ui/a/login")
        driver.find_element_by_id("legPerCod").clear()
        driver.find_element_by_id("legPerCod").send_keys("20000")
        driver.find_element_by_id("depCod").clear()
        driver.find_element_by_id("depCod").send_keys("20005")
        driver.find_element_by_id("tranFrom").clear()
        driver.find_element_by_id("tranFrom").send_keys("47")
        driver.find_element_by_id("opr").clear()
        driver.find_element_by_id("opr").send_keys("1")
        driver.find_element_by_id("i-submit").click()
        time.sleep(5)
    
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
