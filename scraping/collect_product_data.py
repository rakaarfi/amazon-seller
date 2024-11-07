from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class ProductDataCollector:
    """Collect data from a list of product pages."""
    def __init__(self, navigator, extractor, collector, driver_setup):
        """
        notice that when we declaring navigator and extractor
        it actually use the driver from driver_setup

        it will be a good idea to re-use the driver_setup
        example:
        self.navigator = PageNavigator(driver_setup)
        self.extractor = DataExtractor(driver_setup)
        self.collector = DataCollector()
        self.wait = driver_setup.wait # this one might not be needed if you use example on how i find a#sellerProfileTriggerId
        """
        self.navigator = navigator
        self.extractor = extractor
        self.collector = collector
        self.wait = driver_setup.wait

    def collect_data_from_products(self, product_links):
        """Collect data from a list of product pages."""
        for link in product_links:
            self.navigator.driver.get(link)
            try:
                # # Wait for the seller button to appear
                # self.wait.until(EC.visibility_of_element_located(
                #     (By.CSS_SELECTOR, 'div#desktop_qualifiedBuyBox')))

                # # Wait to see if the seller button appears within the timeout
                # seller_button = self.wait.until(EC.presence_of_element_located(
                #     (By.CSS_SELECTOR, "a#sellerProfileTriggerId")))
                # print('Found seller button')  # Only print this if seller button is indeed found
                # seller_button.click()

                """
                use wait only if the element is rendered by javascript
                below code will directly check if the element is present or not
                and execute directly without waiting
                """

                seller_button = self.navigator.driver.find_element(By.CSS_SELECTOR, "a#sellerProfileTriggerId")
                if seller_button:
                    seller_button.click()

                """
                It's look like there is a bug for current_url data.
                If we open the url from the provided excel file, example:
                https://www.amazon.com/sp?ie=UTF8&amp;seller=A1JGTWPBX7NK4E&amp;asin=B085W92DL4&amp;ref_=dp_merchant_link&amp;isAmazonFulfilled=1

                it will redirect us to 
                https://www.amazon.com/gp/help/customer/display.html
                """

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
                
                #self.navigator.go_back() # it seems unnecessary

            except (NoSuchElementException, TimeoutException):
                print("No seller button found or other error, skipping product.")
                """
                IMPROVEMENT SUGGESTIONS:
                - Add monitoring on which product have seller button
                - Add counter to monitor the progress

                in this way you can give a report to your clients such us:
                this keyword has 60 products, 30 of them have seller button
                """
                continue
