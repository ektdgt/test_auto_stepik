from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

# from test_auto_stepik.lesson_2_4_step7 import browser

class TestRegistration(unittest.TestCase):
    def test_1(self):
        self.link = "https://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
        first_name = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        first_name.send_keys("Ivan")
        last_name = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        last_name.send_keys("Petrov")
        email = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        email.send_keys("test@testest.test")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        final_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual('Congratulations! You have successfully registered!', final_text, 'Registration failed')

    def test_2(self):
        self.link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
        first_name = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your name']")
        first_name.send_keys("Ivan")
        last_name = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        last_name.send_keys("Petrov")
        email = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        email.send_keys("test@testest.test")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        final_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual('Congratulations! You have successfully registered!', final_text, 'Registration failed')

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
