import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class DataExtractor:
    """Extract information from a given webpage."""
    def __init__(self, driver_setup):
        self.driver = driver_setup.driver
        self.wait = driver_setup.wait

    @staticmethod
    def get_text(driver, selector_type, selector, fallback="Not Found"): # fallback params is not necessary
        """Get text from an element safely with a fallback value."""
        try:
            if selector_type == 'id':
                element = driver.find_element(By.ID, selector)
            elif selector_type == 'css':
                element = driver.find_element(By.CSS_SELECTOR, selector)
            elif selector_type == 'xpath':
                element = driver.find_element(By.XPATH, selector)
            else:
                raise ValueError("Unsupported selector type")
            
            return element.text.strip() if element else fallback # better to directly "Not Found"
        except NoSuchElementException:
            return fallback

    def get_seller_info(self):
        """Get seller information from the page."""
        
        # Get the seller name
        seller_name = self.get_text(self.driver, 'id', 'seller-name')

        # Get the seller's ratings count
        rating_css = 'a.a-link-normal.feedback-detail-description.no-text-decoration'
        rating_text = self.get_text(self.driver, 'css', rating_css, "No Rating Found")
        start = rating_text.find('(') + 1
        end = rating_text.find(')')
        ratings = rating_text[start:end] if start > 0 and end > start else "No Rating Found"

        # Get the business name
        business_xpath = "//span[contains(text(), 'Business Name:')]/following-sibling::span"
        business_name = self.get_text(self.driver, 'xpath', business_xpath)

        # Get the country from the last element in the address list
        address_css = "div.a-row.a-spacing-none.indent-left"
        address_elements = self.driver.find_elements(By.CSS_SELECTOR, address_css)
        country = address_elements[-1].text.strip() if address_elements else "Country Not Found"
        # If the text is longer than 3 characters, treat it as "Country Not Found"
        country = country if len(country) <= 3 else "Country Not Found"

        # Get the current url
        current_url = self.driver.current_url

        return seller_name, ratings, business_name, country, current_url

    def get_rating_info(self, time_period_button_id, rating_num_id, star_percentage_id, period_label):
        """Get the rating count and 5-star percentage for a specific time period."""
        retries = 3
        for attempt in range(retries):
            try:
                # Click on the time button to toggle the menu
                time_xpath = '//*[@id="seller-rating-time-periods"]/span/span'
                time_button = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, time_xpath)))
                time_button.click()

                # Click on the time period button
                period_button = self.wait.until(EC.element_to_be_clickable(
                    (By.ID, time_period_button_id)))
                period_button.click()

                # Retrieve the rating count
                rating_count_wait = self.wait.until(EC.visibility_of_element_located(
                    (By.ID, rating_num_id)))
                rating_count = rating_count_wait.find_element(By.CLASS_NAME, 'ratings-reviews-count').text

                # Retrieve the 5-star percentage
                star_percentage = self.wait.until(EC.visibility_of_element_located(
                    (By.ID, star_percentage_id))).text

                return rating_count, star_percentage
            except TimeoutException:
                print(f"Attempt {attempt + 1} failed to load {period_label} rating info. Retrying...")
                time.sleep(3)
                if attempt == retries - 1:
                    return "timeout", "timeout"
                