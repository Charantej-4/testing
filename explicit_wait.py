from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
wait=WebDriverWait(driver,10)
username=wait.until(EC.visibility_of_element_located((By.ID,"username"))).send_keys("tomsmith")
password=driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
login=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"radius"))).click()
input("press enter to close")
