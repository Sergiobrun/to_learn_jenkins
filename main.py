import unittest
from selenium import webdriver

class TestsBl(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('https://www.ebay.com/')

    def test_falopa(self):
        print("hola")


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()