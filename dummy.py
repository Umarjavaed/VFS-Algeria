def general_consulate_barcelona(driver, By, WebDriverWait, Ec):
    search_input = WebDriverWait(driver, 20).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Search"]')))
    search_input.click()
    search_input.send_keys('gen')
    target_element = WebDriverWait(driver, 20).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, '.cursor-pointer.pl-4.pr-1\\.5.py-4.border-b.border-zinc-200')))
    target_element.click()

def dummy_category_of_consular_art(driver, By, WebDriverWait, Ec):
    button = WebDriverWait(driver, 200).until(Ec.element_to_be_clickable((By.NAME, 'Select the Consular Act Category')))
    button.click()
    target_element = WebDriverWait(driver, 60).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, 'div.option.cursor-pointer.pl-4.pr-1\\.5.py-4.border-b.border-zinc-200[aria-label="select the Civil Identification Documents option for categoria')))
    target_element.click()

def dummy_consular_art(driver, By, WebDriverWait, Ec, time):
    consular_art_button = WebDriverWait(driver, 20).until(Ec.element_to_be_clickable((By.NAME, 'Select the Consular Act')))
    consular_art_button.click()
    certification_sign = WebDriverWait(driver, 20).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="select the Citizen card collection option for ato"]')))
    certification_sign.click()
    button = WebDriverWait(driver, 20).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[name="Next"][aria-label="Next"][title="Next"]')))
    button.click()
    time.sleep(2)
    button.click()

def schedule_citizen_choose_date(driver, By, WebDriverWait, Ec, time):
    element = WebDriverWait(driver, 20).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, '.w-full.h-\\[60px\\].flex.justify-between.items-center.border.border-slate-400.rounded.px-4')))
    # Click on the element
    element.click()

    element_2 = WebDriverWait(driver, 20).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, '.w-full.h-\\[60px\\].flex.justify-between.items-center.border.border-slate-400.rounded.px-4')))
    element_2.click()

def wait_for_element(driver, by, value, Ec, WebDriverWait, timeout=10):
    return WebDriverWait(driver, timeout).until(Ec.presence_of_all_elements_located((by, value)))

def click_last_navigation(driver,sleep, name, By):
    nav_buttons = driver.find_elements(By.NAME, name)
    if nav_buttons:
        nav_buttons[-1].click()
        print(f"Clicked on last occurrence of navigation button: {name}")
        sleep(3)
    else:
        print(f"Navigation button with name='{name}' not found.")

def find_and_click_normal_button(driver, By, WebDriverWait,sleep, Ec):
    try:
        buttons = driver.find_elements(By.CSS_SELECTOR, '[name="day"][role="gridcell"][type="button"]')
        for button in buttons:
            if button.is_enabled():
                print("Normal button found and clicked.")
                button.click()
                sleep(3)

                # Click the last occurrence of the specific class element
                target_elements = driver.find_elements(By.CSS_SELECTOR, '.w-full.h-full.flex.items-center.gap-x-1')
                if target_elements:
                    last_element = target_elements[-1]
                    last_element.click()
                    print("Clicked on the last occurrence of the target element.")
                    sleep(2)

                    # Click on any enabled hour-slot
                    hour_slots = driver.find_elements(By.CSS_SELECTOR, '[name="hour-slot"]:not([aria-disabled="true"])')
                    if hour_slots:
                        hour_slots[0].click()
                        print("Clicked on the first enabled hour-slot.")
                    else:
                        print("No enabled hour-slot found.")
                else:
                    print("No target element with the specified classes found.")
                return True

        print("No normal button found.")
        return False
    except Exception as e:
        print(f"Error while finding or clicking buttons: {e}")
        return False

def navigate_and_retry(driver, By, WebDriverWait,sleep, Ec):
    navigation_sequence = ["next-month", "next-month", "previous-month", "previous-month", "next-month"]
    for name in navigation_sequence:
        click_last_navigation(driver,sleep, name, By)
        if find_and_click_normal_button(driver, By, WebDriverWait,sleep, Ec):
            return
    print("Retrying navigation sequence...")
    navigate_and_retry(driver, By, WebDriverWait,sleep, Ec)