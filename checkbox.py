from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")
checkboxes=driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
checkbox1=checkboxes[0]
print("Before clicking:",checkbox1.is_selected())
checkbox1.click()
print("After clicking:",checkbox1.is_selected())
input("press enter to close")