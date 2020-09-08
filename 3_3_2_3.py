import unittest
from selenium import webdriver
browser = webdriver.Chrome()


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser.get("http://suninjuly.github.io/registration1.html")
        browser.find_element_by_xpath("//div[@class='first_block']/div[1]/input[1]").send_keys("Michael")
        browser.find_element_by_xpath("//div[@class='first_block']/div[2]/input[1]").send_keys("Jackson")
        browser.find_element_by_xpath("//div[@class='first_block']/div[3]/input[1]").send_keys("k.p@test.qw")
        browser.find_element_by_css_selector("button.btn").click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_abs2(self):
        browser.get("http://suninjuly.github.io/registration2.html")
        browser.find_element_by_xpath("//div[@class='first_block']/div[1]/input[1]").send_keys("Michael")
        browser.find_element_by_xpath("//div[@class='first_block']/div[2]/input[1]").send_keys("Jackson")
        browser.find_element_by_xpath("//div[@class='first_block']/div[3]/input[1]").send_keys("k.p@test.qw")
        browser.find_element_by_css_selector("button.btn").click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
