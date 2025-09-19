import streamlit as st

def render():
    # st.warning("**Disclaimer:** This is an educational tool and not financial advice. All data is provided for informational purposes only. Data may have delays or errors. Please verify the data with your own sources before making any investment decisions.")

    st.write("Concentration risk is a key concept in portfoliio management. It is the risk that a single investment or a small group of investments will perform poorly, causing a significant loss of value. This is especially important for investors who are heavily invested in a single stock or sector.")
    st.write("Traditionally, individual investors have addressed concentration risk by buying well-diversified index funds. However, this assumption has shifted in recent years as the biggest companies now account for a larger percentage of the most widely-held indices.")
    st.write("This app allows you to analyze the concentration risk of your portfolio by determining your portfolio's exposure to individual stocks based on the index funds you hold.")
    st.write("To get started, please visit [Alphavantage](https://www.alphavantage.co/support/#api-key) and request a free API key. Then, input your API key in the sidebar.")