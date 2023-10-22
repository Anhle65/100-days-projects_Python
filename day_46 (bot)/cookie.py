from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/test/")
times = 0
while times <= 120:
    cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
    cookie.click()
    times += 1

print(driver.find_element(By.XPATH, '//*[@id="cookies"]').text)
