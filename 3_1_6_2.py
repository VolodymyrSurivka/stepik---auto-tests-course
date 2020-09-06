import math
from selenium import webdriver
import time


site_link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()

try:
    browser.get(site_link)
    code = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    link = browser.find_element_by_partial_link_text(code)
    time.sleep(1)
    link.click()
    time.sleep(1)
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    time.sleep(1)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
# for git
