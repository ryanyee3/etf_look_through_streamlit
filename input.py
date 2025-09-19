import streamlit as st
import pandas as pd
import ast
import yfinance as yf

def get_last_close(ticker):
    ticker = yf.Ticker(ticker)
    return ticker.history(period='1d')['Close'][0]

def render():

    # --- API Key Input ---
    # st.subheader("Alphavantage API Key")
    # st.info("Please visit https://www.alphavantage.co/support/#api-key to get your free API key. Note that you only get 25 requests per day with a free account. Results are cached for one week.")
    # st.session_state.API_KEY = st.text_input("Enter your API Key", placeholder="")

    # api_key_input = st.text_input(
    #     "Enter your API Key", 
    #     type="password",
    #     help="Get your API key from [Your API Provider's Website](https://example.com)"
    # )

    # # Store the key in session state if it's entered
    # if api_key_input:
    #     st.session_state.api_key = api_key_input
    #     st.success("API Key saved!")

    # --- Nested Tabs for Input Methods ---
    st.subheader("Build Your ETF Portfolio")
    input_method_tab1, input_method_tab2 = st.tabs(["Add Manually", "Paste from Text"])
    
    # --- Method 1: Add Manually ---
    with input_method_tab1:
        with st.form(key='ticker_form', clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                ticker = st.text_input('ETF Ticker')
            with col2:
                shares = st.number_input('Number of Shares', min_value=0, step=1)
            
            submitted = st.form_submit_button('Add to Portfolio')

        if submitted and ticker:
            # Merge with existing portfolio
            st.session_state.portfolio[ticker.upper()] = shares
            st.success(f"Added/Updated {shares} shares of {ticker.upper()}")

    # --- Method 2: Paste from Text ---
    with input_method_tab2:
        st.write("Upload your portfolio data as a JSON with ticker as the key and number of shares as the value.")
    
        # Example format to guide the user
        st.code('# Example JSON \n{"SPY": 100, "QQQ": 150, "VTI": 200, "IBIT": 100, "GLD": 50}')
        
        text_input = st.text_area("Paste your portfolio data here:", height=150)
        
        if st.button("Load Portfolio from Text"):
            if text_input:
                try:
                    # Safely parse the string input into a Python dictionary
                    pasted_data = ast.literal_eval(text_input)
                    
                    # Basic validation
                    if isinstance(pasted_data, dict):
                        # This will replace the existing portfolio
                        st.session_state.portfolio = {str(k).upper(): v for k, v in pasted_data.items()}
                        st.success("Successfully loaded portfolio from text!")
                        st.rerun()
                    else:
                        st.error("Invalid format. The pasted text must be a dictionary.")
                        
                except Exception as e:
                    st.error(f"An error occurred: Please check the format of your text. Details: {e}")
    
    # --- Display the Current Portfolio ---
    st.header('Current Portfolio')
    if not st.session_state.portfolio:
        st.info("Your portfolio is empty.")
    else:
        df = pd.DataFrame(list(st.session_state.portfolio.items()), 
                          columns=['Ticker', 'Shares'])
        df['Last Close'] = df['Ticker'].apply(get_last_close)
        df['Total Value'] = df['Shares'] * df['Last Close']
        df.set_index('Ticker', inplace=True)
        st.dataframe(df.style.format({'Last Close': '${:,.2f}', 'Total Value': '${:,.2f}'}), use_container_width=True)
        st.session_state.portfolio_df = df.copy()
        st.write(f"Total Portfolio Value: ${df['Total Value'].sum():,.2f}")

        if st.button('Clear Portfolio'):
            st.session_state.portfolio = {}
            st.rerun()