import os
import json
import time
import subprocess
from selenium import webdriver
# import selenium


def site_login(driver):
	url = "https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin"
	with open("../metadata/credentials.json") as f:
		credentials = json.load(f)

	driver.get(url)
	driver.find_element_by_id("username").send_keys(credentials["username"])
	driver.find_element_by_id("password").send_keys(credentials["password"])
	driver.find_element_by_css_selector("button[type='submit']").click();
	time.sleep(5)
	return

driver = webdriver.Chrome()
site_login(driver)