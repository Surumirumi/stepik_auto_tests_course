from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submitButton = browser.find_element(By.XPATH, "//button[@type='submit']")
    submitButton.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    firstNum = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    answer = str(math.log(abs(12*math.sin(int(firstNum)))))
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(answer)

    submitButton = browser.find_element(By.XPATH, "//button[@type='submit']")
    submitButton.click()

    print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    browser.quit()