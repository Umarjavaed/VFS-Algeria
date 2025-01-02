import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from dependencies import *  # My Personal Functions File
import random
from selenium.webdriver.common.keys import Keys
import os
from pyautogui import press
from pyautogui import typewrite
from time import sleep
import time

try:
    url = "https://agendamentos.mne.gov.pt/en/login"
    while True:
        try:
            chrome_options = options(uc, os)  # Set Chrome options
            driver = uc.Chrome(options=chrome_options)  # Create Chrome WebDriver instance
            driver.maximize_window()
            setup_extension(press, sleep, typewrite, driver, By)
            driver.get("https://www.google.com/")
            print("Loading The Proxy")
            sleep(2)
            get_api_key(driver, sleep,Keys, By, random, WebDriverWait, Ec)
            driver.get(url)
            sleep(2)

            does_text_exist = "Appointments at the consular offices and at the customer service office in Lisbon" in driver.page_source or "Marcações nos Postos Consulares e no Gabinete Atendimento ao Público em Lisboa" in driver.page_source

            if does_text_exist:
                print("Page Loaded Successfully!")
                accept_all = "Aceitar todas" in driver.page_source or "Accept all" in driver.page_source
                if accept_all:
                    click_accept_button(driver, By)
                    result = click_element_by_text(driver, By, Ec, WebDriverWait)
                    if result:  # Check if the click was successful
                        print("Clicked On Result!")
                        type_user_and_pass(driver, sleep, random, WebDriverWait, Ec, By)  # Fixed: removed unnecessary 'time' argument
                        submit(driver, By, sleep, WebDriverWait, Ec)
                        open_consular_posts(driver, By,Ec, WebDriverWait, sleep)
                        click_consular_office_button(driver, Ec, WebDriverWait, By)
                        click_and_type(driver, By, WebDriverWait, Ec)
                        category_of_consular_art(driver, By, WebDriverWait, Ec)
                        consular_art(driver, By, WebDriverWait, Ec, sleep)
                        find_and_click_day_button(driver,time, Ec, By, WebDriverWait)
                        sleep(10000)
                        break  # Exit the loop if successful
                    else:
                        print("Result Not Found!")
                        driver.quit()
                        sleep(2)
            else:
                print("Page Not Found!")
                driver.quit()
                sleep(2)
        except Exception as e:
            print(f"An error occurred: {e}")
            sleep(2)
finally:
    driver.quit()
