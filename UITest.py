import os
import time
from datetime import datetime
from selenium import webdriver

# resolutions list
resolutions = {    'Desktop': ['1920x1080', '1366x768', '1536x864'],
    'Mobile': ['360x640', '414x896', '375x667']}

# browsers list
browsers = ['chrome', 'firefox']

# create directory if it doesn't exist
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# screenshots
def take_screenshot(driver, folder_name, resolution):
    create_directory(folder_name)
    # window size based on resolution
    width, height = resolution.split('x')
    driver.set_window_size(int(width), int(height))
    # Capture screenshot
    screenshot_path = os.path.join(folder_name, f'Screenshot-{datetime.now().strftime("%Y%m%d-%H%M%S")}.png')
    driver.save_screenshot(screenshot_path)

# run test for each combination of browser, resolution, and URL
def run_test(url):
    for browser in browsers:
        for device, resolutions_list in resolutions.items():
            for resolution in resolutions_list:
                print("Current browser, device, resolution", browser, device, resolution)
                if browser == 'chrome':
                    driver = webdriver.Chrome()
                elif browser == 'firefox':
                    driver = webdriver.Firefox()
                # elif browser == 'safari':
                #     print("Safari not installed ATM")
                    # driver = webdriver.Safari()
                else:
                    print(f'Unsupported browser: {browser}')
                    continue
                
                driver.get(url)

                folder_name = os.path.join('Screenshot', browser.capitalize(), device, resolution)
                take_screenshot(driver, folder_name, resolution)
                
                driver.quit()


if __name__ == "__main__":
    urls = [
        "https://www.getcalley.com/",
        "https://www.getcalley.com/calley-call-from-browser/"
        # "https://www.getcalley.com/calley-pro-features/", 
        # "https://www.getcalley.com/best-auto-dialer-app/",
        # "https://www.getcalley.com/how-calley-auto-dialer-app-works/"
        ]
    for url in urls:
        print("Current URL", url)
        run_test(url)
        print(time.sleep(5))
