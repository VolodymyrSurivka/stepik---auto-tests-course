from selenium import webdriver
import math
import time

browser = webdriver.Chrome()


def result(x_qwe1):
    return str(math.log(abs(12 * math.sin(int(x_qwe1)))))


try:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element_by_tag_name("button.btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_qwe = int(browser.find_element_by_id("input_value").text)
    y = result(x_qwe)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_tag_name("button.btn").click()
finally:
    time.sleep(10)
    browser.quit()
