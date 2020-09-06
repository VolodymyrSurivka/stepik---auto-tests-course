from selenium import webdriver
import time
import math


def res(x_el4):
    return str(math.log(abs(12 * math.sin(int(x_el4)))))


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element_by_tag_name("button.trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id("input_value").text
    y = res(x)
    browser.find_element_by_name("text").send_keys(y)
    browser.find_element_by_tag_name("button.btn").click()
finally:
    time.sleep(10)
    browser.quit()
print(y)
# for git
