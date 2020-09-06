from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


# site_link = "http://suninjuly.github.io/selects1.html"
site_link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()

try:
    browser.get(site_link)
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(int(x) + int(y)))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
