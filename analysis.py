import streamlit as st
import requests
import os
import pandas as pd
import json
import plotly.express as px

# --- data fetching function ---
# caches data for 7 days
@st.cache_data(ttl="7d")
def get_etf_profile(ticker):
    if 'api_key' not in st.session_state:
        raise Exception('API Key not found in session state. Please input your API Key in the sidebar.')
    else:
        try:
            api_key = st.session_state.api_key
            url = f'https://www.alphavantage.co/query?function=ETF_PROFILE&symbol={ticker}&apikey={api_key}'
            r = requests.get(url)
            return r.json()
        except Exception as e:
            raise Exception(f"An error occurred while fetching the ETF profile for {ticker}: {str(e)}")


def render():
    # st.warning("**Disclaimer:** This is an educational tool and not financial advice. All data is provided for informational purposes only. Data may have delays or errors. Please verify the data with your own sources before making any investment decisions.")

    # Check if portfolio exists
    if 'portfolio' not in st.session_state:
        st.error('Portfolio not found in session state. Please input your portfolio in the "Portfolio Input" tab.')
        return
    
    # Check if portfolio is not empty
    if not st.session_state.portfolio:
        st.warning('Please input your portfolio in the "Portfolio Input" tab.')
        return
    
    try:
        # fetch etf profiles for each ticker in portfolio
        etf_profiles = {}
        for ticker in st.session_state.portfolio.keys():
            etf_profiles[ticker] = get_etf_profile(ticker)
            if etf_profiles[ticker] is None:
                st.error(f"Failed to fetch profile for {ticker}. Please check your API Key and try again.")
                return

        # get list of all holdings
        holdings = {}
        for etf in st.session_state.portfolio.keys():
            tmp = etf_profiles[etf]["holdings"]
            for stock in tmp:
                allocation = float(stock["weight"]) * st.session_state.portfolio_df.loc[etf, 'Total Value']
                if stock["symbol"] not in holdings:
                    holdings[stock["symbol"]] = {"value": allocation}
                else:
                    holdings[stock["symbol"]]["value"] += allocation

        # compute percentage of portfolio value for each holding
        portfolio_value = st.session_state.portfolio_df['Total Value'].sum()
        for stock in holdings:
            holdings[stock]["pct"] = holdings[stock]["value"] / portfolio_value

        # get S&P 500 weights
        sp500_profile = get_etf_profile("SPY")
        sp500_weights = {}
        for stock in sp500_profile["holdings"]:
            sp500_weights[stock["symbol"]] = float(stock["weight"])

        # record S&P 500 weights for each holding
        for stock in holdings:
            if stock in sp500_weights:
                holdings[stock]["sp500_weight"] = sp500_weights[stock]
                holdings[stock]["diff"] = holdings[stock]["pct"] - holdings[stock]["sp500_weight"]
            else:
                holdings[stock]["sp500_weight"] = 0.0
                holdings[stock]["diff"] = holdings[stock]["pct"] - holdings[stock]["sp500_weight"]
        
        # Create DataFrame for display
        df_data = []
        for symbol, data in holdings.items():
            df_data.append({
                'Ticker': symbol,
                'Value ($)': data['value'],
                '% Portfolio': data['pct'],
                '% S&P 500': data['sp500_weight'],
                'Difference': data['diff'],
            })
            # df_data.append({
            #     'Ticker': symbol,
            #     'Value ($)': f"${data['value']:,.2f}",
            #     '% Portfolio': f"{data['pct']:.2%}",
            #     '% S&P 500': f"{data['sp500_weight']:.2%}",
            #     'Difference': f"{data['diff']:.2%}"
            # })
        
        df = pd.DataFrame(df_data)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Portfolio Allocation")
            fig1 = px.pie(
                df, 
                names='Ticker', 
                values='% Portfolio'
            )
            fig1.update_traces(textinfo='none', hovertemplate='<b>%{label}</b><br>% Portfolio: %{value:.2%}<extra></extra>')
            fig1.update_layout(showlegend=False)
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            st.subheader("S&P 500 Allocation")
            fig2 = px.pie(
                df, 
                names='Ticker', 
                values='% S&P 500'
            )
            fig2.update_traces(textinfo='none', hovertemplate='<b>%{label}</b><br>% S&P 500: %{value:.2%}<extra></extra>')
            fig2.update_layout(showlegend=False)
            st.plotly_chart(fig2, use_container_width=True)


        # fig = px.pie(df, names='Ticker', values='% Portfolio', title='Portfolio Distribution')
        # fig.update_traces(textinfo='none')
        # fig.update_layout(showlegend=False)
        # fig.update_traces(hovertemplate='<b>%{label}</b><br>Shares: %{value}<extra></extra>')
        # st.plotly_chart(fig, use_container_width=True)

        st.subheader("Detailed Data")
        st.dataframe(df.style.format({'Value ($)': '${:,.2f}', '% Portfolio': '{:.2%}', '% S&P 500': '{:.2%}', 'Difference': '{:.2%}'}), use_container_width=True)
        
    except Exception as e:
        st.error(f"{str(e)}")


