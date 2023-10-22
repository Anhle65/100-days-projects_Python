from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Using ID (no need to have # before the ID) and then get the tag to print text

# articles = driver.find_element(By.ID, "articlecount")
# print(articles.find_element(By.TAG_NAME, 'a').text)

# Using selector (must including # before the ID)
articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

print(articles.text)
articles.click()