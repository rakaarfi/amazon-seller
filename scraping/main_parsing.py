from scraping.setup_driver import DriverSetup
from scraping.navigate_page import PageNavigator
from scraping.extract_data import DataExtractor
from scraping.collect_data import DataCollector
from scraping.collect_product_data import ProductDataCollector


def parsing(save_as):
    # Setup the driver and page navigator
    driver_setup = DriverSetup()
    navigator = PageNavigator(driver_setup)
    extractor = DataExtractor(driver_setup)
    collector = DataCollector()
    product_collector = ProductDataCollector(navigator, extractor, collector, driver_setup) # too long, see my notes on this class

    # Open the search results page for kitchen products
    url_kitchen_products = 'https://www.amazon.com/s?k=kitchen+products&_encoding=UTF8&content-id=amzn1.sym.2f889ce0-246f-467a-a086-d9a721167240&pd_rd_r=ea966871-2e40-4557-a8a1-14161ddb29ec&pd_rd_w=IHkec&pd_rd_wg=lakyL&pf_rd_p=2f889ce0-246f-467a-a086-d9a721167240&pf_rd_r=41R7Z4RR96GJH60GHD9J&ref=pd_hp_d_atf_unk'
    # it can be shortened to
    url_kitchen_products = 'https://www.amazon.com/s?k=kitchen+products'
    navigator.open_url(url_kitchen_products)

    # Get all product links from the search results page
    all_links = navigator.get_product_links()

    # Collect data from the product pages
    product_collector.collect_data_from_products(all_links)

    # Save the collected data to an Excel file
    collector.save_to_excel(save_as)

    # Close the driver
    driver_setup.close()