from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
username=driver.find_element(By.ID,"username").send_keys("tomsmith")
password=driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
Login=driver.find_element(By.CLASS_NAME,"radius").click()
input("press enter to close")