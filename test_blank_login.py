import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("")
driver.find_element(By.NAME, "password").send_keys("")
driver.find_element(By.XPATH, "//button[@id='submit']").click()
time.sleep(5)
print("not logged in")
driver.quit()