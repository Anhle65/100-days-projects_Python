from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://tinder.com/app/recs")
# person = driver.find_element(By.CLASS_NAME, "Scale(.5)")
# person.send_keys(Keys.ENTER)
time.sleep(5)
log_in = driver.find_element(By.XPATH, '//*[@id="u-1535117240"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log_in.click()
time.sleep(5)
email_regist = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div[1]')
email_regist.click()
time.sleep(5)
base_window = driver.window_handles[0]
email_login = driver.window_handles[1]
driver.switch_to.window(email_login)
print(driver.title)