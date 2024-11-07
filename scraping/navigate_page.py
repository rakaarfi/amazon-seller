from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageNavigator:
    """Navigate to a given URL and interact with the page"""
    def __init__(self, driver_setup):
        self.driver = driver_setup.driver
        self.wait = driver_setup.wait

    def open_url(self, url):
        """
        Navigate to a given URL and refresh the page 3 times to ensure
        all elements are loaded.
        """
        self.driver.get(url)

        """
        if Sorry! Something went wrong!

        """

        while self.driver.title == "Sorry! Something went wrong!":
            self.driver.refresh()

        # self.driver.refresh()
        # self.driver.refresh()
        # self.driver.refresh()

    def wait_for_user_to_solve_captcha(self):
        print("Please solve the CAPTCHA manually and press Enter to continue...")
        input("Press Enter to continue after solving the CAPTCHA...")
        submit_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit_button.click()

    def search_product(self, search_query):
        input_product = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="twotabsearchtextbox"]')))
        input_product.send_keys(search_query)
        search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-search-submit-button"]')))
        search_button.click()

    def get_product_links(self):
        """Retrieve product links from the search results page."""

        # Wait for the product list container
        class_name = 's-main-slot.s-result-list.s-search-results.sg-row'
        self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, class_name)))

        # Get all product elements in the page
        css_all_elements = "div.sg-col-4-of-24.sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16"
        all_elements = self.driver.find_elements(By.CSS_SELECTOR, css_all_elements)

        # Get the link within each product element
        css_each_element = 'a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal'
        product_links = []
        for element in all_elements:
            link = element.find_element(By.CSS_SELECTOR, css_each_element).get_attribute('href')
            product_links.append(link)

        return product_links

    def go_back(self):
        self.driver.back()
        """
        it seems unnecessary
        """