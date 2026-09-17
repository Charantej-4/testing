from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
dropdown_element=driver.find_element(By.ID,"dropdown")
dropdown=Select(dropdown_element)
dropdown.select_by_value("2")
time.sleep(20)
driver.quit()