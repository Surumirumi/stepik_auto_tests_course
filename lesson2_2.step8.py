from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os 
import math

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')     

    firstName = browser.find_element(By.XPATH, "//input[@name='firstname']")
    firstName.send_keys("Anton")


    lastName = browser.find_element(By.XPATH, "//input[@name='lastname']")
    lastName.send_keys("Kolesov")

    email = browser.find_element(By.XPATH, "//input[@name='email']")
    email.send_keys("pro100skyanton@mail.ru")

    checkbox = browser.find_element(By.CSS_SELECTOR, "#file")
    checkbox.send_keys(file_path)
    
    submitButton = browser.find_element(By.XPATH, "//button[@type='submit']")
    submitButton.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()