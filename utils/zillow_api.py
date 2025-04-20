import requests

def get_average_home_price(city, state):
    url = "https://zillow-zestimate.p.rapidapi.com/search"
    querystring = {"location": f"{city}, {state}"}
    headers = {
        "X-RapidAPI-Key": "8bdb8fa84fmsh3091226847b6f80p141ab9jsn6db0179b335e",  # Replace with your actual key
        "X-RapidAPI-Host": "zillow-zestimate.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        print("Error fetching data:", response.status_code, response.text)
        return None

    results = response.json().get("results", [])
    prices = []

    for r in results:
        price = r.get("priceZestimate") or r.get("price")  # fallback if Zestimate is missing
        if isinstance(price, (int, float)):
            prices.append(price)

    return sum(prices) / len(prices) if prices else None
