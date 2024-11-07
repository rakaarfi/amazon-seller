from selenium.webdriver.support.ui import WebDriverWait


class WaitDriver:
    """Handles the waiting time."""
    def __init__(self, driver_setup):
        self.driver = driver_setup
        self.wait = WebDriverWait(self.driver, 5)
