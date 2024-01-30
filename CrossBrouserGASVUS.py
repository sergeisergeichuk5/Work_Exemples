import time
import unittest

from faker import Faker
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker()


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search_weather_chrome(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')

        self.assertEquals("California Real Estate – QA at Silicon Valley Real Estate", driver.title, "wrong page title")
        print("Page title in Chrome is:", driver.title)

        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='g2-name']")))
        time.sleep(1)  # simulate long running test

        driver.minimize_window()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)

        # find buttom submit
        submit = driver.find_element(By.XPATH, "//input[@id='g2-name']")
        body = driver.find_element(By.XPATH, "//input[@id='g2-name']")
        if submit:
            submit.click()
        elif driver.body.send_keys(Keys.PAGE_DOWN):
            submit.click()

        name = driver.find_element(By.NAME, "g2-name")
        name.clear()
        name.submit()
        time.sleep(1)
        # fake name
        name = driver.find_element(By.ID, "g2-name")
        name.send_keys(fake.first_name())
        time.sleep(1)

        # scrol down
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        # name.click()
        email = driver.find_element(By.NAME, "g2-email")
        email.clear()
        time.sleep(1)

        # email.send_keys(random_email)
        email = driver.find_element(By.ID, "g2-email")
        email.send_keys(fake.email())
        time.sleep(1)

        # text.send_keys(random_email)

        newsletter = driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']")
        newsletter.click()
        newsletter.send_keys('Hello, World')
        time.sleep(1)

        submit = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        body = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        submit.click()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_search_weather_firefox(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')

        self.assertEquals("California Real Estate – QA at Silicon Valley Real Estate", driver.title, "wrong page title")
        print("Page title in Chrome is:", driver.title)

        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='g2-name']")))
        time.sleep(1)

        driver.minimize_window()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)

        # find buttom submit
        submit = driver.find_element(By.XPATH, "//input[@id='g2-name']")
        body = driver.find_element(By.XPATH, "//input[@id='g2-name']")
        if submit:
            submit.click()
        elif driver.body.send_keys(Keys.PAGE_DOWN):
            submit.click()

        name = driver.find_element(By.NAME, "g2-name")
        name.clear()
        name.submit()
        time.sleep(1)
        # fake name
        name = driver.find_element(By.ID, "g2-name")
        name.send_keys(fake.first_name())
        time.sleep(1)

        # scrol down
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        email = driver.find_element(By.NAME, "g2-email")
        email.clear()
        time.sleep(1)

        email = driver.find_element(By.ID, "g2-email")
        email.send_keys(fake.email())
        time.sleep(1)

        newsletter = driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']")
        newsletter.click()
        newsletter.send_keys('Hello, World')
        time.sleep(1)

        submit = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        body = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        submit.click()


class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def test_search_weather_edge(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')

        self.assertEquals("California Real Estate – QA at Silicon Valley Real Estate", driver.title, "wrong page title")
        print("Page title in Chrome is:", driver.title)

        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='g2-name']")))
        time.sleep(1)

        driver.minimize_window()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)

        submit = driver.find_element(By.XPATH, "//input[@id='g2-name']")
        body = driver.find_element(By.XPATH, "//input[@id='g2-name']")
        if submit:
            submit.click()
        elif driver.body.send_keys(Keys.PAGE_DOWN):
            submit.click()

        name = driver.find_element(By.NAME, "g2-name")
        name.clear()
        name.submit()
        time.sleep(1)
        # fake name
        name = driver.find_element(By.ID, "g2-name")
        name.send_keys(fake.first_name())
        time.sleep(1)

        # scrol down
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        email = driver.find_element(By.NAME, "g2-email")
        email.clear()
        time.sleep(1)

        email = driver.find_element(By.ID, "g2-email")
        email.send_keys(fake.email())
        time.sleep(1)

        newsletter = driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']")
        newsletter.click()
        newsletter.send_keys('Hello, World')
        time.sleep(1)

        submit = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        body = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        submit.click()


if __name__ == "__main__":
    unittest.main()
