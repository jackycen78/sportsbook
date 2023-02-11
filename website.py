from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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
            EC.visibility_of_any_elements_located((By.XPATH, xpath))
        )[0]

    def class_locate(self, class_name, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_any_elements_located((By.CLASS_NAME, class_name))
        )

    def class_locate_all(self, class_name, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_any_elements_located((By.CLASS_NAME, class_name))
        )

    def find_child_by_class(self, parent, childClassName, time = 2):
        try: 
            return WebDriverWait(parent, time).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, childClassName))
            )[0]
        except TimeoutException:
            return None

    def click(self, location, time=10):        
        self.locate(location, time).click()

    def enter_text(self, location, text):
        self.locate(location).send_keys(text)

    def enter_and_clear_text(self, location, text):
        self.locate(location).clear()
        self.locate(location).send_keys(text)