from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.google.com")
search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("selenium with python")
search_box.send_keys(Keys.ENTER)
input("press enter to close")