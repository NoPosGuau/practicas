from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com")

#enter the name, email, phone number, and text in the textarea
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

#click on the button "male" and "monday" and "friday"
web_element = driver.find_element(By.ID, "male")
web_element.click()

web_element = driver.find_element(By.ID, "monday")
web_element.click()

web_element = driver.find_element(By.ID, "friday")
web_element.click()

time.sleep(15)