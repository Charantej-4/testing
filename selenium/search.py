from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.google.com")
search_box=driver.find_element(By.NAME,"q")
input("press enter to close")