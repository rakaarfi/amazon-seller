from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class ProductDataCollector:
    """Collect data from a list of product pages."""
    def __init__(self, navigator, extractor, collector, driver_setup):
        self.navigator = navigator
        self.extractor = extractor
        self.collector = collector
        self.wait = driver_setup.wait

    def collect_data_from_products(self, product_links):
        """Collect data from a list of product pages."""
        for link in product_links:
            self.navigator.driver.get(link)
            try:
                # Wait for the seller button to appear
                self.wait.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'div#desktop_qualifiedBuyBox')))

                # Wait to see if the seller button appears within the timeout
                seller_button = self.wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "a#sellerProfileTriggerId")))
                print('Found seller button')  # Only print this if seller button is indeed found
                seller_button.click()

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
                
                self.navigator.go_back()
            except (NoSuchElementException, TimeoutException):
                print("No seller button found or other error, skipping product.")
                continue
