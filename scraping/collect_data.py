import pandas as pd


class DataCollector:
    """Collect and store data."""
    def __init__(self):
        self.data = {
            "Seller Name": [], "Ratings Count": [], "Business Name": [], "Country": [],
            "30 Days Rating Count": [], "30 Days 5 Star Percentage": [],
            "90 Days Rating Count": [], "90 Days 5 Star Percentage": [],
            "12 Months Rating Count": [], "12 Months 5 Star Percentage": [],
            "Lifetime Rating Count": [], "Lifetime 5 Star Percentage": [], "URL": []
        }

    def add_seller_info(self, seller_name, ratings, business_name, country, current_url):
        """Add seller information to the data dictionary."""
        self.data["Seller Name"].append(seller_name)
        self.data["Ratings Count"].append(ratings)
        self.data["Business Name"].append(business_name)
        self.data["Country"].append(country)
        self.data["URL"].append(current_url)

    def add_rating_info(self, period, rating_count, star_percentage):
        """Add rating information to the data dictionary."""
        self.data[f"{period} Rating Count"].append(rating_count)
        self.data[f"{period} 5 Star Percentage"].append(star_percentage)

    def save_to_excel(self, filename):
        df = pd.DataFrame(self.data)
        df.to_excel(filename, index=False)