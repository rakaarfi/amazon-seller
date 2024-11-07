from selenium.webdriver.support.ui import WebDriverWait


class WaitDriver:
    """Setup and manage the WebDriver instance."""
    def __init__(self, driver_setup):
        self.driver = driver_setup
        self.wait = WebDriverWait(self.driver, 5)
