import time

from selenium import webdriver
from selenium.webdriver.common.by import By
def perform_login():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.NAME, "password").send_keys("Password123")
    driver.find_element(By.XPATH, "//button[@id='submit']").click()

    time.sleep(3)
    try:
        assert "Logged In Successfully" in driver.page_source
        print("positive test flow passed")
    except AssertionError:
        driver.save_screenshot("login_failure")


    driver.find_element(By.XPATH, "//a[normalize-space()='Log out']").click()
    assert "This is a simple Login page. Students can use this page to practice writing simple positive and negative LogIn tests. Login functionality is something that most of the test automation engineers need to automate" in driver.page_source
    print("Logged out successfully")
    time.sleep(5)
    driver.quit()

perform_login()