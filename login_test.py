# Task 2B: Automated Testing with AI
# Objective: Automate login test cases for valid and invalid credentials using Selenium.
# Author: Buseiry

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome browser
driver = webdriver.Chrome()

# Open a sample login page (replace this with your test site if available)
driver.get("https://practicetestautomation.com/practice-test-login/")

# VALID login test
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

# Take screenshot of result
driver.save_screenshot("results/screenshots/valid_login.png")

# Go back to login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# INVALID login test
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

# Take screenshot of invalid login result
driver.save_screenshot("results/screenshots/invalid_login.png")

# Close browser
driver.quit()
