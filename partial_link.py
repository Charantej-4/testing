from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
link=driver.find_element(By.PARTIAL_LINK_TEXT,"authentication").click()
input("press enter to close")
