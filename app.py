import streamlit as st
import json
from pathlib import Path
import guide
import input
import analysis

st.title("Porfolio Look-Through Analysis")

# 1. Initialize the dismiss state if it doesn't exist
if 'disclaimer_dismissed' not in st.session_state:
    st.session_state.disclaimer_dismissed = False

# 2. Conditionally display the disclaimer
if not st.session_state.disclaimer_dismissed:
    st.warning("⚠️ **Disclaimer:** This is an educational tool and not financial advice. All data is provided for informational purposes only. Data may have delays or errors. Please verify the data with your own sources before making any investment decisions.")
    # 3. Create a button to dismiss the disclaimer
    if st.button("I understand and wish to dismiss"):
        st.session_state.disclaimer_dismissed = True
        st.rerun()

# --- Tab Creation ---
tab1, tab2, tab3 = st.tabs(["Guide", "Input", "Analysis"])

# --- Initialize Session State ---
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = {}

# --- Place the API key input in the sidebar ---
with st.sidebar:
    st.header("Configuration")
    api_key_input = st.text_input(
        "Enter your API Key", 
        type="password",
        help="Get your free API key from [Alphavantage](https://www.alphavantage.co/support/#api-key)"
    )

    # Store the key in session state if it's entered
    if api_key_input:
        st.session_state.api_key = api_key_input
        st.success("API Key saved!")

# --- Tab 1: User Guide ---
with tab1:
    guide.render()

# --- Tab 2: Portfolio Input ---
with tab2:
    input.render()

# --- Tab 3: Analysis ---
with tab3:
    analysis.render()
