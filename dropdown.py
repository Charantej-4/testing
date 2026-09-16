from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
dropdown_element=driver.find_element(By.ID,"dropdown")
dropdown=Select(dropdown_element)
dropdown.select_by_visible_text("option 1")
input("press enter to close")
time.sleep(20)
