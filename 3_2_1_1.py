from selenium import webdriver
import time
import math


def calc(x_question):
    return str(math.log(abs(12 * math.sin(int(x_question)))))


site_link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    browser.get(site_link)
    x_element = browser.find_element_by_id("input_value")
    time.sleep(1)
    x_ques = x_element.text
    y = calc(x_ques)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector('[value="robots"]')
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
# for git
