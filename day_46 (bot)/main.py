from selenium import webdriver
from selenium.webdriver.common.by import By


# chrome_driver_path = "C:/development/chromedriver.exe"
# driver = webdriver.Chrome()
# driver.get("https://wise.com/vn/currency-converter/nzd-to-vnd-rate")
# price = driver.find_element(By.CLASS_NAME, 'text-success')
# print(price.text)


# driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()

driver2.get("https://www.mbbank.com.vn/ExchangeRate")
# rate = driver1.find_element(By.CSS_SELECTOR, ".table-fee td")
rate1 = driver2.find_element(By.XPATH, '//*[@id="BODY"]/div[5]/div/div[4]/div/div/table/tbody/tr[10]/td[5]')
print(rate1.text)