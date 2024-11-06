from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


class DriverSetup:
    """Setup and manage the WebDriver instance."""
    def __init__(self):
        options = Options()
        options.add_argument('--start-maximized')
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 20)

    def close(self):
        self.driver.quit()