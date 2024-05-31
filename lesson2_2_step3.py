from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstNum = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    secondNum =  int(browser.find_element(By.CSS_SELECTOR, "#num2").text)

    sumAnswer = str(firstNum + secondNum)


    listEl = Select(browser.find_element(By.CSS_SELECTOR, ".custom-select"))
    listEl.select_by_value(sumAnswer)

    submitButton = browser.find_element(By.XPATH, "//button[@type = 'submit']")
    submitButton.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit(