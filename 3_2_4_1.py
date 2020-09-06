from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import math
import time


def result(x_qwe1):
    return str(math.log(abs(12 * math.sin(int(x_qwe1)))))


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), str(100)))
    browser.find_element_by_id("book").click()
    x_qwe = int(browser.find_element_by_id("input_value").text)
    y = result(x_qwe)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id("solve").click()
finally:
    time.sleep(10)
    browser.quit()
