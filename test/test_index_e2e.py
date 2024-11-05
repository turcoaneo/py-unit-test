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
        heading = self.find_text_by_id_css('h1', self.heading_title)
        self.assertEqual(self.expected_text, heading)

    def test_page_has_input_text(self):
        input_element = self.find_text_by_id_css('input', 'input-text')
        self.assertIsNotNone(input_element)

    def test_page_has_submit_button(self):
        button = self.find_text_by_id_css('button', 'submit-button')
        self.assertIsNotNone(button)

    def test_page_has_table(self):
        input_element = self.find_element_by_id_css('input', 'input-text')
        button = self.find_element_by_id_css('button', 'submit-button')
        input_element.send_keys('France and Germany share a border in Europe')
        button.click()
        table = self.find_element_by_id_css('table', 'table-result')
        self.assertIsNotNone(table)

    def find_element_by_id_css(self, tag, value):
        return WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, tag + "[data-test-id='" + value + "']")))

    def find_text_by_id_css(self, tag, value):
        return self.find_element_by_id_css(tag, value).text

    def find_by_id(self, value):
        return WebDriverWait(self.driver, 2).until(
            ec.visibility_of_element_located((By.XPATH, "//h1[@data-test-id='" + value + "']"))).text

    def find(self, value):
        return self.driver.find_element("id", value).text
