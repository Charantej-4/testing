from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
username=driver.find_element(By.XPATH,"//input@id='username']").send_keys("tomsmith")
password=driver.find_element(By.XPATH,"//input@id='password']").send_keys("SuperSecretPassword!")
login=driver.find_elementBy.XPATH,"//button@type='submit']".click()
input("press enter to close")
time.sleep(20)