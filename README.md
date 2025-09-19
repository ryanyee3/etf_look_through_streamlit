# ETF Portfolio Look-Through Analysis Tool

A Streamlit-based web application that analyzes portfolio concentration risk by performing "look-through" analysis on ETF holdings. This tool helps investors understand their actual exposure to individual stocks through their ETF investments and compare it against S&P 500 weights.

## Overview

This application addresses the growing concern about concentration risk in modern portfolios. As the largest companies now represent a larger percentage of major indices, traditional diversification through index funds may not provide the expected risk reduction. This tool performs a "look-through" analysis to reveal the underlying stock holdings of your ETF portfolio and compares your actual exposure to S&P 500 weights.

## Features

- **Portfolio Input**: Two methods for adding ETF holdings:
  - Manual entry of ticker symbols and share quantities
  - Bulk import via JSON text input
- **Real-time Pricing**: Fetches current stock prices using Yahoo Finance
- **Look-through Analysis**: Retrieves underlying holdings of each ETF using Alpha Vantage API
- **Visualization**: Interactive pie charts comparing portfolio allocation vs S&P 500 allocation
- **Detailed Reporting**: Comprehensive data table showing individual stock exposures and differences

## Architecture

The application is built with a modular structure using Streamlit:

### Core Files

- **`app.py`**: Main application entry point
  - Sets up the Streamlit interface with tabs
  - Manages session state for portfolio data and API key
  - Handles disclaimer display and dismissal
  - Coordinates between different modules

- **`input.py`**: Portfolio input management
  - `get_last_close()`: Fetches current stock prices using yfinance
  - `render()`: Creates the portfolio input interface with two methods:
    - Manual entry form for individual ETF additions
    - Text area for bulk JSON import
  - Displays current portfolio with real-time valuations

- **`analysis.py`**: Core analysis engine
  - `get_etf_profile()`: Cached function to fetch ETF holdings from Alpha Vantage API
  - `render()`: Performs look-through analysis and generates visualizations
  - Calculates portfolio concentration and compares against S&P 500 weights
  - Creates interactive charts using Plotly

- **`guide.py`**: User guidance and documentation
  - `render()`: Displays educational content about concentration risk
  - Explains the purpose and methodology of the tool

## Dependencies

The application requires the following Python packages:

```
streamlit>=1.49.1
pandas>=2.3.2
plotly>=6.3.0
yfinance>=0.2.66
requests>=2.32.5
```

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd etf_look_through_streamlit
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install streamlit pandas plotly yfinance requests
   ```

4. **Get an Alpha Vantage API key**:
   - Visit [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
   - Sign up for a free account (25 requests per day)
   - Copy your API key

5. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Configure API Key**: Enter your Alpha Vantage API key in the sidebar
2. **Build Portfolio**: Use either input method in the "Input" tab:
   - **Manual Entry**: Add ETFs one by one with ticker and share count
   - **Bulk Import**: Paste JSON format: `{"SPY": 100, "QQQ": 150, "VTI": 200}`
3. **View Analysis**: Navigate to the "Analysis" tab to see:
   - Portfolio allocation pie chart
   - S&P 500 allocation comparison
   - Detailed holdings table with concentration metrics

## Data Sources

- **Stock Prices**: Yahoo Finance (via yfinance library)
- **ETF Holdings**: Alpha Vantage API
- **S&P 500 Weights**: SPY ETF holdings (via Alpha Vantage)

## API Rate Limits

- **Alpha Vantage Free Tier**: 25 requests per day
- **Caching**: ETF profile data is cached for 7 days to minimize API calls
- **Efficient Usage**: The app fetches each ETF profile only once per session

## Key Functions

### Portfolio Management
- Real-time portfolio valuation using current market prices
- Support for both individual and bulk portfolio entry
- Session state persistence across page refreshes

### Look-through Analysis
- Fetches underlying holdings for each ETF in the portfolio
- Calculates weighted exposure to individual stocks
- Compares portfolio concentration against S&P 500 benchmark

### Data Visualization
- Interactive pie charts for portfolio and S&P 500 allocations
- Formatted data tables with percentage and dollar value displays
- Hover tooltips for detailed information

## Error Handling

The application includes comprehensive error handling for:
- Missing API keys
- Invalid ticker symbols
- Network connectivity issues
- Malformed JSON input
- API rate limit exceeded

## Development Guidelines

### Code Structure
- Each module has a single `render()` function for Streamlit integration
- Session state is used for data persistence across tabs
- Caching is implemented for expensive API calls

### Adding New Features
1. Create new functions in appropriate modules
2. Add new tabs in `app.py` if needed
3. Update session state management as required
4. Follow Streamlit best practices for UI components

### Testing
- Test with various portfolio configurations
- Verify API key handling and error states
- Check data formatting and visualization accuracy

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes following the existing code style
4. Test thoroughly with different portfolio configurations
5. Submit a pull request with a clear description of changes

## License

This project is for educational purposes only. Please ensure compliance with Alpha Vantage and Yahoo Finance terms of service when using their APIs.

## Disclaimer

This tool is for educational purposes only and does not constitute financial advice. All data is provided for informational purposes and may have delays or errors. Users should verify data with their own sources before making investment decisions.
