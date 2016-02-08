from selenium import webdriver
import unittest

class NewEventTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_serving_empty_webpage(self):  
        self.browser.get('http://localhost:8000')
        self.assertIn('Django', self.browser.title)  

if __name__ == '__main__':  
    unittest.main() 