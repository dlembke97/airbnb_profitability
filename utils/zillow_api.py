import requests

def get_average_home_price(city, state):
    url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"
    querystring = {"location": f"{city}, {state}"}
    headers = {
        "X-RapidAPI-Key": "YOUR_API_KEY",
        "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    listings = response.json().get("props", [])
    if not listings:
        return None

    prices = [l.get("price", 0) for l in listings if l.get("price")]
    return sum(prices) / len(prices) if prices else None
