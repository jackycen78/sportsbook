from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class Website:

    def __init__(self) -> None:

        service = Service('./chromedriver')
        options = ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')

        self.driver = Chrome(options=options, service=service)
        self.driver.set_window_size(1720, 1329)
        self.driver.set_window_position(0, 0)

    def go_to(self, website, sleepTime=1):
        self.driver.get(website)
        time.sleep(sleepTime)

    def find_xpath(self, xpath, waitSeconds=5):
        try: 
            return WebDriverWait(self.driver, waitSeconds).until(
            EC.visibility_of_any_elements_located((By.XPATH, xpath))
        )[0]
        except TimeoutError:
            return None

    def find_class(self, className, parent=None, waitSeconds=5):
        if not parent:
            parent = self.driver
        try: 
            return WebDriverWait(parent, waitSeconds).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, className))
            )
        except TimeoutException:
            return [None]
        
    def class_exists(self, className, parent=None, waitSeconds=2): 
        if self.find_class(className, parent, waitSeconds) == [None]:
            return False
        return True
        
    def click_by_xpath(self, location, waitSeconds=2, sleepTime=0):        
        self.locate(location, waitSeconds).click()
        time.sleep(sleepTime)

    def click_by_class(self, className, parent=None, waitSeconds=2, sleepTime=0):
        buttons = self.find_class(className, parent, waitSeconds, sleepTime)
        if buttons != [None]:
            for b in buttons:
                b.click()
            time.sleep(sleepTime)

    def enter_text(self, location, text):
        self.locate(location).send_keys(text)

    def enter_and_clear_text(self, location, text):
        self.locate(location).clear()
        self.locate(location).send_keys(text)