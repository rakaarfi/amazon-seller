# Amazon Seller and Product Data Scraper
This repository contains a web scraper built to extract detailed information about Amazon sellers and their products. It collects data such as seller name, ratings, business details, and reviews across different time periods, saving the output in an Excel file.

## Table of Contents
- [Features](#Features)
- [Project Structure](#Project-Structure)
- [Requirements](#Requirements)
- [Usage](#Usage)
- [Customization](#Customization)
- [Copyright](#Copyright)
  
## Features
- Scrapes Amazon seller and product information from Amazon search results.
- Extracts details like seller name, business name, ratings, country, and 5-star review percentages over time.
- Exports data to an Excel file for easy access and analysis.
  
## Project Structure
- **main.py**: Entry point for running the scraper. Sets up command-line arguments and initiates the scraping process.
- **main_parsing.py**: Coordinates the main scraping workflow, including navigation, data collection, and saving.
- **setup_driver.py**: Configures the Selenium WebDriver, optimizing options for headless scraping and improved speed.
- **wait_driver.py**: Manages wait times, ensuring elements are loaded before interactions.
- **navigating_page.py**: Handles navigation tasks on Amazon, including page loads and product link extraction.
- **collect_data.py**: Structures and stores the extracted data, supporting seller and rating details.
- **collect_product_data.py**: Collects seller information for each product in a specified category.
- **extract_data.py**: Extracts specific data fields using CSS and XPath selectors.

## Requirements
- Python 3.x
- [Selenium WebDriver](https://www.selenium.dev/)
- Chrome browser and ChromeDriver
  
Install dependencies using:
```
pip install -r requirements.txt
```
> Note: Ensure that the correct version of ChromeDriver is installed for your Chrome version.

## Usage
To run the scraper and save the data to an Excel file, use:
```
python main.py --save_as "output_file.xlsx"
```
- `--save_as` (optional): Specifies the name of the output Excel file. Defaults to `seller_info.xlsx` if not provided.
### Example
```
python main.py --save_as "amazon_seller_data.xlsx"
```
This will start the scraper and save the results in an Excel file named `amazon_seller_data.xlsx`.

## Customization
- **Target URL**: You can modify the Amazon search URL in `main_parsing.py` to scrape data for different product categories..
- **Data Fields**: Update fields or add new ones in `collect_data.py` if you need additional information from the listings.

## Copyright
Copyright©2024 ***Raka Arfi***

Released under MIT License
