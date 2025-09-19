import streamlit as st

def render():

    # st.write("Concentration risk is a key concept in portfolio management. It is the risk that a single investment or a small group of investments will perform poorly, causing a significant loss of value. This is especially important for investors who are heavily invested in a single stock or sector.")
    # st.write("Traditionally, individual investors have addressed concentration risk by buying well-diversified index funds. However, this assumption has shifted in recent years as the biggest companies now account for a larger percentage of the most widely-held indices.")
    # st.write("This app allows you to analyze the concentration risk of your portfolio by determining your portfolio's exposure to individual stocks based on the index funds you hold.")
    # st.write("To get started, please visit [Alphavantage](https://www.alphavantage.co/support/#api-key) and request a free API key. Then, input your API key in the sidebar.")

    st.subheader("Is your portfolio diversified? You might be surprised.")

    st.markdown("""
    Even if you only own "diversified" index funds like the S&P 500, a handful of mega-cap stocks
    (like Apple, Microsoft, and NVIDIA) may secretly dominate your portfolio. This is known as **concentration risk**,
    and it means your investments might not be as safe as you think.
    """)

    st.subheader("What This App Does 💡")

    st.markdown("""
    This tool looks *inside* your ETFs to reveal your true, underlying exposure to individual stocks.

    **How it works:**
    1. **Enter Your API Key:** Visit [Alphavantage](https://www.alphavantage.co/support/#api-key) and request a free API key (no email verification required). Input your API key in the sidebar.
    2. **Enter Your ETFs:** Tell us which index funds you hold and the number of shares on the "Input" tab.
    3. **We Analyze the Holdings:** The app pulls the latest data for what's inside each fund.
    4. **See Your True Exposure:** Discover your total ownership of individual stocks, aggregated across all your funds.

    Find out if you're truly diversified or if you're unintentionally making a massive bet on just a few companies.
    """)

    # st.subheader("Getting Started")

    # st.markdown("""
    # To get started, please visit [Alphavantage](https://www.alphavantage.co/support/#api-key) and request a free API key. Then, input your API key in the sidebar.
    # """)
