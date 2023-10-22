from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")
account = driver.find_element(By.NAME, value="fName")
account.send_keys("ANH")
family = driver.find_element(By.NAME, value="lName")
family.send_keys("LE")
email = driver.find_element(By.NAME, value="email")
email.send_keys("abc@gmail.com")
register = driver.find_element(By.CLASS_NAME, "btn-block")
register.send_keys(Keys.ENTER)
