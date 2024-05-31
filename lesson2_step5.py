from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = "#treasure"
    x_element = browser.find_element(By.CSS_SELECTOR, x_value)
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answerInput = browser.find_element(By.CSS_SELECTOR, "#answer")
    answerInput.send_keys(y)

    checkbox_value = "#robotCheckbox"
    checkbox = browser.find_element(By.CSS_SELECTOR, checkbox_value)
    checkbox.click()

    radio_value = "#robotsRule"
    radio = browser.find_element(By.CSS_SELECTOR, radio_value)
    radio.click()
    
    submitButton = browser.find_element(By.XPATH, "//button[@type = 'submit']")
    submitButton.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
