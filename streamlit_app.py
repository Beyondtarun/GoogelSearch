from pytrends.request import TrendReq
import streamlit as st
import pandas as pd

st.title("🔍 Google Search Trends in India")
keyword = st.text_input("Enter a topic (e.g., cricket, AI, finance):")

if keyword:
    try:
        pytrends = TrendReq(hl='en-IN', tz=330)
        pytrends.build_payload([keyword], geo='IN')

        related_queries = pytrends.related_queries()

        # Check if 'related_queries' has data and keyword exists
        if related_queries and keyword in related_queries:
            rising = related_queries[keyword].get('rising')
            top = related_queries[keyword].get('top')

            if rising is not None and not rising.empty:
                st.subheader(f"🔥 Rising Searches for '{keyword}':")
                st.dataframe(rising.head(10))

            elif top is not None and not top.empty:
                st.subheader(f"📈 Top Searches for '{keyword}':")
                st.dataframe(top.head(10))

            else:
                st.info(f"No rising or top related queries found for '{keyword}'. Try another one.")
        else:
            st.warning(f"Google returned no related query data for '{keyword}'.")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
