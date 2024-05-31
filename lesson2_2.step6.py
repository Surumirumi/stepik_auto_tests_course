from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = " https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstNum = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    answer = str(math.log(abs(12*math.sin(int(firstNum)))))
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(answer)

    submitButton = browser.find_element(By.XPATH, "//button[@type = 'submit']")

    browser.execute_script("return arguments[0].scrollIntoView(true);", submitButton)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()


    radioButton = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    radioButton.click()




    submitButton.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()