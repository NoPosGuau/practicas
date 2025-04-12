from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com")

# Wait for the page to load
time.sleep(5)
web_element = driver.find_element(By.ID, "name")
web_element.send_keys("Samuel Romney")
time.sleep(2)
web_element = driver.find_element(By.ID, "email")
web_element.send_keys("SR@TEST.COM")
time.sleep(2)
web_element = driver.find_element(By.ID, "phone")
web_element.send_keys("1234567890")
web_element = driver.find_element(By.ID, "textarea")
web_element.send_keys("esto es un nuevo cambio. ")

time.sleep(15)