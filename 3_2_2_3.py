from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
try:
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Michael")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Jackson")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("k.p@test.qw")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    loader = browser.find_element_by_name("file")
    loader.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
finally:
    time.sleep(10)
    browser.quit()
