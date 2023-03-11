from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium_stealth import stealth
import time

class Website:

    def __init__(self) -> None:

        service = Service('./chromedriver')
        options = ChromeOptions()
        options.add_argument("start-maximized")
        #options.add_argument("--headless")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
        options.add_experimental_option("useAutomationExtension", False) 

        self.driver = Chrome(options=options, service=service)
        '''stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )'''
        
        #self.go_to('https://www.bet365.com/#/AC/B18/C20604387/D48/E1453/F10/')
        #time.sleep(10)

    def go_to(self, website, sleepTime=1):
        self.driver.get(website)
        time.sleep(sleepTime)

    def find_xpath(self, xpath, waitSeconds=1):
        try: 
            return WebDriverWait(self.driver, waitSeconds).until(
            EC.visibility_of_any_elements_located((By.XPATH, xpath))
        )[0]
        except TimeoutError:
            return None

    def find_class(self, className, parent=None, waitSeconds=2):
        if not parent:
            parent = self.driver
        try: 
            return WebDriverWait(parent, waitSeconds).until(
                EC.visibility_of_any_elements_located((By.CLASS_NAME, className))
            )
        except TimeoutException:
            return [None]
        
    def find_name(self, name, path='', parent=None, waitSeconds=5, exact=False):
        if not parent:
            parent = self.driver
        try: 
            string = f"//*[contains(text(),'{name}')]{path}"
            if exact: 
                string = f'//*[text() = "{name}"]{path}'
            return WebDriverWait(parent, waitSeconds).until(
                EC.visibility_of_any_elements_located((By.XPATH, string))
            )
        except TimeoutException:
            return [None]
        
    def class_exists(self, className, parent=None, waitSeconds=2): 
        if self.find_class(className, parent, waitSeconds) == [None]:
            return False
        return True
        
    def click_by_xpath(self, location, waitSeconds=2, sleepTime=0):        
        self.find_xpath(location, waitSeconds).click()
        time.sleep(sleepTime)

    def click_by_class(self, className, parent=None, waitSeconds=2, sleepTime=0):
        buttons = self.find_class(className, parent, waitSeconds)
        if buttons != [None]:
            for b in buttons:
                b.click()
            time.sleep(sleepTime)

    def click_by_name(self, name, path='', parent=None, waitSeconds=2, exact=False):
        button = self.find_name(name, path, parent, waitSeconds, exact)[0]
        if button:
            button.click()

    def refresh_page(self):
        self.driver.refresh()
        time.sleep(1)

    def enter_text(self, location, text):
        self.locate(location).send_keys(text)

    def enter_and_clear_text(self, location, text):
        self.locate(location).clear()
        self.locate(location).send_keys(text)