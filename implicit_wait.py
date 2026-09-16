from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com")
search=driver.find_element(By.NAME,"q").send_keys("selenium python")
input("press enter to close")

