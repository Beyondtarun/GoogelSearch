from pytrends.request import TrendReq
import streamlit as st
import pandas as pd

st.title("🔍 Google Search Trends in India")
keyword = st.text_input("Enter a topic (e.g., fitness, tech, finance):")

if keyword:
    pytrends = TrendReq(hl='en-IN', tz=330)
    pytrends.build_payload([keyword], geo='IN')

    related_queries = pytrends.related_queries()

    if keyword in related_queries and related_queries[keyword]['rising'] is not None:
        rising = related_queries[keyword]['rising']
        st.subheader(f"🔥 Rising Searches for '{keyword}':")
        st.dataframe(rising.head(15))
    else:
        st.warning(f"No rising search queries found for '{keyword}'. Try another topic.")
