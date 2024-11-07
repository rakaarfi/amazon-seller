from scraping.collect_product_data import ProductDataCollector


def parsing(save_as):
    # Initialize objects
    product_collector = ProductDataCollector()

    # Open the search results page for kitchen products
    url_kitchen_products = 'https://www.amazon.com/s?k=kitchen+products'
    product_collector.navigator.open_url(url_kitchen_products)

    # Get all product links from the search results page
    all_links = product_collector.navigator.get_product_links()

    # Collect data from the product pages
    product_collector.collect_data_from_products(all_links)

    # Save the collected data to an Excel file
    product_collector.collector.save_to_excel(save_as)
