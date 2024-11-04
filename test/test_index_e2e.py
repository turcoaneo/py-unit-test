import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class E2ETests(unittest.TestCase):
    expected_text = 'Name Entity Finder'
    heading_title = 'heading-title'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")

    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn("Named Entity", self.driver.title)

    def test_app_name(self):
        heading = self.find('app-heading')
        self.assertEqual(self.expected_text, heading)

    def test_app_name_by_test_id(self):
        heading = self.find_by_id(self.heading_title)
        self.assertEqual(self.expected_text, heading)

    def test_app_name_by_test_id_css(self):
        heading = self.find_by_id_css(self.heading_title)
        self.assertEqual(self.expected_text, heading)

    def find_by_id_css(self, value):
        return WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, "h1[data-test-id='" + value + "']"))).text

    def find_by_id(self, value):
        return WebDriverWait(self.driver, 2).until(
            ec.visibility_of_element_located((By.XPATH, "//h1[@data-test-id='" + value + "']"))).text

    def find(self, value):
        return self.driver.find_element("id", value).text
