import os
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains


# Configure headless browser options

opts = FirefoxOptions()
opts.add_argument("--headless")

# Start web driver
driver = webdriver.Firefox(options=opts)

# Navigate to Grafana login page
driver.get("http://ip-addr/login")
driver.find_element(By.NAME, "user").click()
driver.find_element(By.NAME, "user").send_keys("admin")
driver.find_element(By.ID, "current-password").click()
driver.find_element(By.ID, "current-password").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, ".css-14g7ilz-button > .css-1mhnkuh").click()
driver.execute_script("window.scrollTo(0,0)")
driver.find_element(By.ID, "url-input").click()
driver.find_element(By.ID, "url-input").send_keys("1860")
driver.find_element(
    By.CSS_SELECTOR, ".css-1sara2j-button:nth-child(1) > .css-1mhnkuh"
).click()
element = driver.find_element(By.CSS_SELECTOR, ".css-1r7wtwe-input-wrapper .css-5dz6jh")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.CSS_SELECTOR, ".css-1kfdb0e")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.CSS_SELECTOR, ".theme-dark").click()
driver.find_element(
    By.CSS_SELECTOR, ".css-59ctgk-grafana-select-option-body > span"
).click()
driver.find_element(
    By.CSS_SELECTOR,
    ".css-cvef6c-layoutChildrenWrapper > .css-1sara2j-button > .css-1mhnkuh",
).click()
element = driver.find_element(By.CSS_SELECTOR, ".css-1a8393j-button > .css-1mhnkuh")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.execute_script("window.scrollTo(0,0)")

# Close browser
driver.close()
