from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverSetup:
    """Setup and manage the WebDriver instance."""
    def __init__(self):
        # Configure Chrome options
        options = Options()
        # Start Chrome in maximized mode to ensure all elements are visible and prevent blocking
        options.add_argument('--start-maximized')
        # Ignore certificate errors, which may cause the browser to fail to load
        options.add_argument('--ignore-certificate-errors')

        # Initialize the Chrome browser with options
        self.driver = webdriver.Chrome(options=options)

    def close(self):
        self.driver.quit()
        