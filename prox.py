import os
import random
import undetected_chromedriver as webdriver

class ProxyExtension:
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {"scripts": ["background.js"]},
        "minimum_chrome_version": "76.0.0"
    }
    """

    background_js = """
    var config = {
        mode: "fixed_servers",
        rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: %d
            },
            bypassList: ["localhost"]
        }
    };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        { urls: ["<all_urls>"] },
        ['blocking']
    );
    """

    def __init__(self, host, port, user, password, directory="proxy_extension"):
        self._dir = os.path.abspath(directory)

        manifest_file = os.path.join(self._dir, "manifest.json")
        with open(manifest_file, mode="w") as f:
            f.write(self.manifest_json)

        background_js = self.background_js % (host, port, user, password)
        background_file = os.path.join(self._dir, "background.js")
        with open(background_file, mode="w") as f:
            f.write(background_js)

    @property
    def directory(self):
        return self._dir


def format_string(input_string):
    split_string = input_string.strip().split(':')
    if len(split_string) == 4:
        return split_string[0], int(split_string[1]), split_string[2], split_string[3]
    else:
        raise ValueError("Input string does not match the expected format.")


def process_proxies():
    file_path = "proxies.txt"
    try:
        with open(file_path, 'r') as file:
            proxies = file.readlines()

        filtered_proxies = [proxy for proxy in proxies if proxy.strip().startswith("na")]

        if filtered_proxies:
            proxy = random.choice(filtered_proxies)
            return format_string(proxy)
        else:
            print("No proxies starting with 'na' found in the file.")
            return None
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except ValueError as e:
        print(f"Error processing proxy: {e}")
        return None


def setup_chrome_with_proxy():
    proxy = process_proxies()
    if proxy:
        host, port, user, password = proxy
        extension = ProxyExtension(host, port, user, password)
        options = webdriver.ChromeOptions()
        options.add_argument(f"--load-extension={extension.directory}")

        try:
            # Initialize Chrome with proxy extension
            driver = webdriver.Chrome(options=options)
            return driver
        except Exception as e:
            print(f"Error starting Chrome: {e}")

    return None

def setup_extension(press, sleep, typewrite, driver, By):
    current_dir = os.getcwd()
    name = "0.4.13_0"
    urban_vpn = "4.11.0_0"
    Nopecha_extension = f"{current_dir}\\{name}"
    Urban_Vpn = f"{current_dir}\\{urban_vpn}"
    driver.get("chrome://extensions")
    sleep(2)
    press("tab")
    press("tab")
    press("tab")
    press("tab")
    press("enter")
    sleep(1)
    press("tab")
    press("enter")
    sleep(2)
    print(f"typing {current_dir}\\{name}")
    typewrite(Nopecha_extension)
    press("enter")
    press("tab")
    press("enter")
    sleep(3)


# Example Usage
if __name__ == "__main__":
    driver = setup_chrome_with_proxy()
    if driver:
        driver.get("https://ipinfo.io/")
        input("Press Enter to continue...")
        # Perform your actions with the driver here
        driver.quit()