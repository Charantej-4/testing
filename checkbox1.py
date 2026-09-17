from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")
checkboxes = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
checkbox1 = checkboxes[0]
checkbox2 = checkboxes[1]
print("Before:")
print("Checkbox 1:", checkbox1.is_selected())
print("Checkbox 2:", checkbox2.is_selected())
if not checkbox1.is_selected():
    checkbox1.click()
if not checkbox2.is_selected():
    checkbox2.click()
print("After:")
print("Checkbox 1:", checkbox1.is_selected())
print("Checkbox 2:", checkbox2.is_selected())
input("Press Enter to close")
driver.quit()