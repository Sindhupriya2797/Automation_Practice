import time

from selenium import webdriver
from selenium.webdriver.common.by import By
def perform_login_invalid():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("Hello")
    driver.find_element(By.NAME, "password").send_keys("Hello")
    driver.find_element(By.XPATH, "//button[@id='submit']").click()

    time.sleep(4)
    try:
        assert "logged in succesfully" in driver.page_source
    except AssertionError:
        driver.save_screenshot("login_error.png")
        raise
    print("page is not logged in")
    driver.quit()

perform_login_invalid()