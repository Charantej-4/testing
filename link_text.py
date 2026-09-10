from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
link=driver.find_element(By.LINK_TEXT,"Form Authentication").click()
input("press enter to close")