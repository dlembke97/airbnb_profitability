import streamlit as st
import pandas as pd
from utils.zillow_api import get_average_home_price
from utils.airbnb_metrics import estimate_airbnb_metrics
from utils.profitability import calculate_profitability

st.title("Airbnb Profitability Analyzer")

city = st.text_input("Enter City", "Peoria")
state = st.text_input("Enter State Abbreviation", "IL")

listings_file = st.file_uploader("Upload InsideAirbnb listings.csv")
calendar_file = st.file_uploader("Upload InsideAirbnb calendar.csv")

if st.button("Analyze") and listings_file and calendar_file:
    df_listings = pd.read_csv(listings_file)
    df_calendar = pd.read_csv(calendar_file)

    df_listings.to_csv("temp_listings.csv", index=False)
    df_calendar.to_csv("temp_calendar.csv", index=False)

    price = get_average_home_price(city, state)
    airbnb_data = estimate_airbnb_metrics("temp_listings.csv", "temp_calendar.csv")
    metrics = calculate_profitability(price, airbnb_data)

    st.subheader(f"Results for {city}, {state}")
    for k, v in metrics.items():
        st.write(f"**{k}**: {v}")
