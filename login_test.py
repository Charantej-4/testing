from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/Login")
username=driver.find_element(By.NAME,"username").send_keys("tomsmith")
password=driver.find_element(By.NAME,"password").send_keys("SuperSecretPassword!")
login=driver.find_element(By.CLASS_NAME,"radius").click()
input("press enter to close")
