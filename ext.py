import os 
from time import sleep
from selenium.webdriver.support import expected_conditions as Ec
from selenium import webdriver
from pyautogui import press
from pyautogui import typewrite

current_dir = os.getcwd()
name = "0.4.13_0"
Nopecha_extension = f"{current_dir}\\{name}"
print(f"{current_dir}\\{name}")

driver = webdriver.Chrome()
driver.get("chrome://extensions")
press("tab")
press("enter")
press("tab")
press("enter")
sleep(2)
typewrite(Nopecha_extension)
press("enter")
press("tab")
press("enter")

input("Press Enter to continue...")
driver.quit()