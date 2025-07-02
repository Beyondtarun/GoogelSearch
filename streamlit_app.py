# streamlit_app.py

import streamlit as st
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# UI
st.title("🔍 Google Search Trends in India")
keyword = st.text_input("Enter a topic (e.g., fitness, tech, finance):")

if keyword:
    pytrends = TrendReq(hl='en-IN', tz=330)
    pytrends.build_payload([keyword], geo='IN')

    rising = pytrends.related_queries()[keyword]['rising']

    if rising is not None:
        st.subheader(f"🔥 Rising Searches for '{keyword}':")
        st.dataframe(rising.head(15))
    else:
        st.warning("No rising queries found.")
