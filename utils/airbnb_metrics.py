import pandas as pd

def estimate_airbnb_metrics(listings_path, calendar_path):
    listings = pd.read_csv(listings_path)
    calendar = pd.read_csv(calendar_path)

    available = calendar[calendar['available'] == 't']
    prices = available['price'].str.replace('$','').str.replace(',','').astype(float)
    adr = prices.mean()

    total_days = calendar.groupby('listing_id').size()
    available_days = calendar[calendar['available'] == 't'].groupby('listing_id').size()
    occupancy = 1 - (available_days / total_days).mean()

    annual_revenue = adr * occupancy * 365

    return {
        'ADR': round(adr, 2),
        'Occupancy': round(occupancy, 2),
        'Annual_Revenue': round(annual_revenue)
    }
