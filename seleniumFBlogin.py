from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By

#ask user for email and password
username = input("Enter your username: ")
password = getpass("Enter your password: ")

#create driver
driver = webdriver.Chrome("C:\\WebDriver\\chromedriver.exe")
driver.get("https://www.facebook.com/")

#finds textboxes by ID
username_txt = driver.find_element(By.ID, "email")
username_txt = driver.send_keys(username)

password_txt = driver.find_element(By.ID, "pass")
password_txt = driver.send_keys(password)

#presses btn
login_button = driver.find_element(By.ID, "u_0_j_W9")
login_button.submit()
