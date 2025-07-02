from pytrends.request import TrendReq
import streamlit as st
import pandas as pd

st.title("🔍 Google Search Trends in India")
keyword = st.text_input("Enter a topic (e.g., fitness, tech, finance):")

if keyword:
    try:
        pytrends = TrendReq(hl='en-IN', tz=330)
        pytrends.build_payload([keyword], geo='IN')

        related_queries = pytrends.related_queries()

        if keyword in related_queries:
            rising = related_queries[keyword].get('rising')
            if rising is not None and not rising.empty:
                st.subheader(f"🔥 Rising Searches for '{keyword}':")
                st.dataframe(rising.head(15))
            else:
                st.info(f"No 'rising' related queries found for '{keyword}'.")
        else:
            st.warning(f"Google Trends returned no data for '{keyword}'. Try another topic.")

    except Exception as e:
        st.error(f"An error occurred: {e}")
