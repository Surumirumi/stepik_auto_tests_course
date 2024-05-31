from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    expected_price = "100"

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), expected_price)
    )

    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    firstNum = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    answer = str(math.log(abs(12*math.sin(int(firstNum)))))
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(answer)

    submitButton = browser.find_element(By.XPATH, "//button[@type='submit']")
    submitButton.click()

    print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    browser.quit()