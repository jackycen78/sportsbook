from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Website:

    def __init__(self) -> None:

        service = Service('./chromedriver')
        options = ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')

        self.driver = Chrome(options=options, service=service)
        self.driver.set_window_size(1720, 1329)
        self.driver.set_window_position(0, 0)

    def go_to(self, website):
        self.driver.get(website)

    def locate(self, xpath, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    def click(self, location, time=10):        
        self.locate(location, time).click()

    def enter_text(self, location, text):
        self.locate(location).send_keys(text)

    def enter_and_clear_text(self, location, text):
        self.locate(location).clear()
        self.locate(location).send_keys(text)