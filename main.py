import argparse

from scraping.main_parsing import parsing

def main():
    """
    Main function to handle command-line arguments and trigger the web scraping and data saving process.

    Command-line Arguments:
    --save_as (str): Optional argument to specify the name of the Excel file to save the data to.
                      Defaults to 'seller_info.xlsx' if not provided.
    """
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Scrape Amazon seller information and save it to an Excel file')
    parser.add_argument('--save_as', type=str, default='seller_info.xlsx', help='Specify the name of the Excel file to save the data to')

    # Parse the arguments
    args = parser.parse_args()

    # Call the parsing function
    parsing(args.save_as)

if __name__ == "__main__":
    main()
