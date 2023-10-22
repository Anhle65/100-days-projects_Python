from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
events_list = {}
driver.get("https://www.python.org/")
event = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu time")
title = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")
i = 0
while i < len(event):
    events_list[i] = {
        "event": title[i].text,
        "time": event[i].text
    }
    i += 1
print(events_list)