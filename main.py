from utils.zillow_api import get_average_home_price
from utils.airbnb_metrics import estimate_airbnb_metrics
from utils.profitability import calculate_profitability

city = "Peoria"
state = "IL"

price = get_average_home_price(city, state)
airbnb_data = estimate_airbnb_metrics(f"data/insideairbnb/{city}_listings.csv",
                                      f"data/insideairbnb/{city}_calendar.csv")

metrics = calculate_profitability(price, airbnb_data)
print(f"--- {city}, {state} ---")
for k, v in metrics.items():
    print(f"{k}: {v}")
