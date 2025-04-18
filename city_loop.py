import pandas as pd
from utils.zillow_api import get_average_home_price
from utils.airbnb_metrics import estimate_airbnb_metrics
from utils.profitability import calculate_profitability

cities = [
    ("Peoria", "IL"),
    ("Fairbanks", "AK"),
    ("Akron", "OH"),
    ("Columbus", "GA")
]

results = []

for city, state in cities:
    print(f"Processing {city}, {state}")
    try:
        price = get_average_home_price(city, state)
        airbnb_data = estimate_airbnb_metrics(f"data/insideairbnb/{city}_listings.csv",
                                              f"data/insideairbnb/{city}_calendar.csv")
        metrics = calculate_profitability(price, airbnb_data)
        metrics['City'] = f"{city}, {state}"
        results.append(metrics)
    except Exception as e:
        print(f"Failed for {city}, {state}: {e}")

df = pd.DataFrame(results)
df.sort_values(by="Cap Rate", ascending=False, inplace=True)
df.to_csv("city_comparison_results.csv", index=False)
print("Results saved to city_comparison_results.csv")
