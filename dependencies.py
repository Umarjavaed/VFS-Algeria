from fake_useragent import UserAgent
from prox import *
from dummy import *

def ua_rotate():
    ua = UserAgent()  # Create a UserAgent instance
    return ua.random  # Generate a random user agent

def options(uc, os):
    
    chrome_options = uc.ChromeOptions()
    # proxy = process_proxies()
    # if proxy:
    #     host, port, user, password = proxy
    #     extension = ProxyExtension(host, port, user, password)
    #     chrome_options.add_argument(f"--load-extension={extension.directory}")
        
    # else:
    #     print("No proxy found.")   
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_experimental_option("prefs", {"credentials_enable_service": False,
        "profile.password_manager_enabled": False})
    fake_user_agent = ua_rotate()
    print(f"Selecting User Agent : {fake_user_agent}")  # Print the fake user-agent for debugging
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument(f"--user-agent={fake_user_agent}")  # Set the fake user agent
    return chrome_options

def click_element_by_text(driver, By, Ec, WebDriverWait):
    texts = [
        "Authentication via credentials",
        "Autenticação via credenciais"
    ]
    # Loop through each text and find the corresponding element
    for text in texts:
        try:
            element = WebDriverWait(driver, 30).until(Ec.presence_of_element_located((By.XPATH, f"//div[text()='{text}']")))
            if element:  # Check if the div element exists
                element.click()  # Click the element if found
                print("Clicked on element")
                try:
                    input_element = WebDriverWait(driver, 5).until(Ec.presence_of_element_located((By.XPATH, "//input[@placeholder='###########']")))
                    return True
                except:
                    return False
        except Exception as e:
            print(f"Error while clicking element: {e}")
            return False  # Return False if no element is clicked

def click_accept_button(driver, By):
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    for button in buttons:
        if button.text.strip() == 'Accept all' or button.text.strip() == 'Aceitar todas':
            button.click()
            return True  # Click and return True when the button is found
    return False  # Return False if the button is not found

def type_user_and_pass(driver, sleep, random, WebDriverWait, Ec, By): 
    user_name = "tiktokbetta.tlm@gmail.com"
    input_field = WebDriverWait(driver, 10).until(Ec.visibility_of_element_located((By.XPATH, '//input[@placeholder="###########"]')))
    for char in user_name:
        random_user_name = random.uniform(0.05, 0.09)
        input_field.send_keys(char)
        sleep(random_user_name)
    comp_password = "Walid@20121996"
    input_field = WebDriverWait(driver, 10).until(Ec.visibility_of_element_located((By.XPATH, '//input[@placeholder="***********"]')))
    for passsword in comp_password:
        random_passsword = random.uniform(0.05, 0.09)
        input_field.send_keys(passsword)
        sleep(random_passsword)
    print("Username and Password Entered Successfully!")

def get_api_key(driver, sleep,Keys, By, random, WebDriverWait, Ec):
    driver.get('chrome-extension://dknlfmjaanfblgfdfebhijalfmhmjjjo/popup.html')
    sleep(5)
    print("Nopecha Opened")                
    sleep(2)
    try:
        button = WebDriverWait(driver, 20).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, '.key-icon.font-normal.color-brand[title="Click to edit"]')))
        button.click()
    except:
        print("No button found")
        
    sleep(2)
    input_element = driver.find_element(By.CSS_SELECTOR, "input.key-input")
    Api_key = "eyezymbljvnqdg60"
    input_value = input_element.get_attribute('value')
    try:
        if input_value:
            print(f"Input value: {input_value}")
            if input_value == Api_key:
                print("Api Key is Correct!")
        else:
            after_delay = random.uniform(0.03, 0.09)
            for char in Api_key:
                input_element.send_keys(char)
                sleep(0.02)
            input_element.send_keys(Keys.ENTER)
            print(input_value)
            sleep(2)
    except Exception as e:
        print(f"Error occurred: {str(e)}")

def check_captcha_solved(driver, WebDriverWait, Ec, By):
    try:
        iframe = WebDriverWait(driver, 10).until(Ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]")))
        checkbox = WebDriverWait(driver, 10).until(Ec.presence_of_element_located((By.ID, 'recaptcha-anchor')))
        aria_checked = checkbox.get_attribute("aria-checked")
        return aria_checked == "true"
    except Exception as e:
        print(f"An error occurred while checking CAPTCHA: {e}")
        return False
    finally:
        driver.switch_to.default_content()

def submit(driver, By, sleep, WebDriverWait, Ec):
    check_captcha_solved(driver, WebDriverWait, Ec, By)
    while True:
        captcha_solved = check_captcha_solved(driver, WebDriverWait, Ec, By)
        if captcha_solved:
            print("CAPTCHA is solved (checkbox is checked).")
            break  # Exit the loop if CAPTCHA is solved
        else:
            print("CAPTCHA is not solved (checkbox is not checked). Checking again...")
            sleep(2)  # Wait for a few seconds before checking again

    button = driver.find_element(By.CSS_SELECTOR, 'div.w-full button[type="submit"][name="Login"][aria-label="Login"]')
    if button is not None and button.is_displayed() and button.is_enabled():
        button.click()

def open_consular_posts(driver, By,Ec, WebDriverWait, sleep):
    wait = WebDriverWait(driver, 200)
    titles = ["Open Consular Post form", "Abrir formulário Posto Consular"]
    for title in titles:
        try:
            element = wait.until(Ec.presence_of_element_located((By.XPATH, f"//*[@title='{title}']")))
            element.click()
            print(f"Clicked on the element with title: {title}")
            return
        except:
            continue
    print("No matching element found for the specified titles.")
    sleep(10000)

def click_consular_office_button(driver, Ec, WebDriverWait, By):
    try:
        button = WebDriverWait(driver, 200).until(Ec.element_to_be_clickable((By.NAME, "Select the Consular Office")))
        button.click()
        print("Button with name 'Select the Consular Office' clicked successfully.")
    except:
        try:
            button = WebDriverWait(driver, 200).until(Ec.element_to_be_clickable((By.NAME, "Selecione o Posto Consular")))
            button.click()
            print("Button with name 'Selecione o Posto Consular' clicked successfully.")
        except:
            print("Neither button found.")

def click_and_type(driver, By, WebDriverWait, Ec):
    search_input = WebDriverWait(driver, 200).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Search"]')))
    search_input.click()
    search_input.send_keys('alg')
    target_element = WebDriverWait(driver, 200).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, '.cursor-pointer.pl-4.pr-1\\.5.py-4.border-b.border-zinc-200')))
    target_element.click()

def category_of_consular_art(driver, By, WebDriverWait, Ec):
    button = WebDriverWait(driver, 200).until(Ec.element_to_be_clickable((By.NAME, 'Select the Consular Act Category')))
    button.click()
    target_element = WebDriverWait(driver, 60).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, 'div.option.cursor-pointer.pl-4.pr-1\\.5.py-4.border-b.border-zinc-200[aria-label="select the Notary  option for categoria"]')))
    target_element.click()

def consular_art(driver, By, WebDriverWait, Ec, sleep):
    consular_art_button = WebDriverWait(driver, 20).until(Ec.element_to_be_clickable((By.NAME, 'Select the Consular Act')))
    consular_art_button.click()
    # Wait for the element with the specific aria-label to be clickable
    certification_sign = WebDriverWait(driver, 20).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="select the Certification of a signature option for ato"]')))
    certification_sign.click()

    button = WebDriverWait(driver, 20).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[name="Next"][aria-label="Next"][title="Next"]')))
    button.click()

    sleep(5)
    try:
        wait = WebDriverWait(driver, 10)  # 10 seconds timeout
        next_button = driver.find_element(By.XPATH, '//button[@name="Next" and @aria-label="Next"]')

        next_button.click()
        print("Next button found and clicked.")
        
    except:
        print("Next button not found.")
        sleep(10000)
    sleep(5)
    if not find_and_click_normal_button(driver, By, WebDriverWait,sleep, Ec):
        navigate_and_retry(driver, By, WebDriverWait,sleep, Ec)

def find_and_click_day_button(driver,time, Ec, By, WebDriverWait):    
    try:
        time.sleep(6)
        driver.execute_script("""
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function clickValidDayButton() {
    const dayButtons = document.querySelectorAll('[name="day"][role="gridcell"]:not([disabled])');
    if (dayButtons.length > 0) {
        dayButtons[0].click(); // Click the first valid day button
        console.log('Clicked on a valid "day" button.');
        await delay(3000); // Wait for potential "hour-slot" buttons to load
        return true;
    }
    console.log('No valid "day" button found.');
    return false;
}

async function clickValidHourSlotButton() {
    const hourSlotButtons = document.querySelectorAll('[name="hour-slot"]:not([disabled])');
    if (hourSlotButtons.length > 0) {
        hourSlotButtons[0].click(); // Click the first valid hour-slot button
        console.log('Clicked on a valid "hour-slot" button.');
        return true;
    }
    console.log('No valid "hour-slot" button found.');
    return false;
}

async function clickNextButton() {
    const nextButton = document.querySelector('[aria-label="Next"]:not([disabled])');
    if (nextButton) {
        nextButton.click(); // Click the "Next" button
        console.log('Clicked on the "Next" button.');
        await delay(3000); // Wait for UI to update
        return true;
    }
    console.log('No valid "Next" button found or it is disabled.');
    return false;
}

async function clickMonthButton(direction) {
    const buttonName = direction === 'next' ? 'next-month' : 'previous-month';
    const buttons = document.querySelectorAll(`[name="${buttonName}"]`);
    if (buttons.length > 0 && !buttons[0].disabled) {
        buttons[0].click(); // Click the next/previous month button
        console.log(`Clicked on the "${direction}-month" button.`);
        await delay(3000); // Wait for the UI to update
        return true;
    }
    console.log(`"${direction}-month" button is disabled.`);
    return false;
}

async function findAndClickDayButton() {
    const startTime = Date.now(); // Record the start time
    const timeLimit = 90 * 1000; // 1 minute 30 seconds in milliseconds
    let direction = 'next'; // Start by moving forward

    while (Date.now() - startTime < timeLimit) {
        // Try clicking a valid day button
        if (await clickValidDayButton()) {
            // If a day button is clicked, try finding and clicking a valid hour-slot button
            if (await clickValidHourSlotButton()) {
                // If both day and hour-slot are clicked, click the "Next" button
                if (await clickNextButton()) {
                    console.log('Process complete after clicking "Next" button.');
                    return true; // Exit the function completely
                }
            } else {
                console.log('Hour-slot not available. Continuing in the same direction.');
            }
        }

        // Navigate based on the current direction
        if (direction === 'next') {
            if (!(await clickMonthButton('next'))) {
                // If the next-month button is disabled, switch to the previous-month direction
                console.log('Next month is disabled. Switching to previous month.');
                direction = 'previous';
            }
        } else {
            if (!(await clickMonthButton('previous'))) {
                // If the previous-month button is disabled, stop the process
                console.log('Previous month is also disabled. Stopping the process.');
                return false;
            }
        }
    }

    console.log('Time limit reached. Stopping the process.');
    return false;
}

async function runProcessInLoop() {
    while (true) {
        console.log('Starting a new process iteration...');
        
        const processCompleted = await findAndClickDayButton();

        if (processCompleted) {
            console.log('Process completed successfully. Exiting the loop.');
            break; // Exit the loop completely if the process is successful
        }

        console.log('Restarting process...');
    }
}

runProcessInLoop();
""")

    except Exception as e:
        print(f"An error occurred: {e}")

