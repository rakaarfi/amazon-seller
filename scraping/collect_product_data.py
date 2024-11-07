from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from scraping.setup_driver import DriverSetup
from scraping.navigate_page import PageNavigator
from scraping.extract_data import DataExtractor
from scraping.collect_data import DataCollector


class ProductDataCollector:
    """Collect data from a list of product pages."""
    def __init__(self):
        self.driver = DriverSetup().driver
        self.navigator = PageNavigator(self.driver)
        self.extractor = DataExtractor(self.driver)
        self.collector = DataCollector()

    def collect_data_from_products(self, product_links):
        """Collect data from a list of product pages."""
        length = len(product_links)
        for idx, link in enumerate(product_links):
            self.driver.get(link)
            print(f'Extracting data {idx + 1} out of {length}...')
            try:
                # Find the seller button
                seller_button = self.driver.find_element(By.CSS_SELECTOR, "a#sellerProfileTriggerId")
                
                # Click the seller button if it exists
                seller_button.click()
                print(f'Found seller button.')  # Only print this if seller button is indeed found

                seller_name, ratings, business_name, country, current_url = self.extractor.get_seller_info()
                self.collector.add_seller_info(seller_name, ratings, business_name, country, current_url)

                for period, (time_id, rating_id, star_id) in {
                    "30 Days": ("rating-dropdown_0", "rating-thirty-num", "percentFiveStar"),
                    "90 Days": ("rating-dropdown_1", "rating-90-num", "percentFiveStar"),
                    "12 Months": ("rating-dropdown_2", "rating-365d-num", "percentFiveStar"),
                    "Lifetime": ("rating-dropdown_3", "rating-lifetime-num", "percentFiveStar")
                }.items():
                    rating_count, star_percentage = self.extractor.get_rating_info(time_id, rating_id, star_id, period)
                    self.collector.add_rating_info(period, rating_count, star_percentage)
            except (NoSuchElementException, TimeoutException):
                print(f"No seller button found, skipping product.")
                continue
