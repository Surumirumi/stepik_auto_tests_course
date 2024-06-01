from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


try:

    class TestAbs(unittest.TestCase):
        def test_for_first_link():
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)
            firstName = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
            firstName.send_keys("test test")
            lastName = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
            lastName.send_keys("test test")
            email = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required]")
            email.send_keys("test test")
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(1)
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            assertEqual("Congratulations! You have successfully registered!", welcome_text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
