import pandas as pd
import yfinance as yf
import numpy as np
from scipy.stats import linregress

# Function to get stock prices
def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data['Adj Close']

# Function to get risk-free rate data (10-year Treasury yield)
def get_risk_free_rate(start_date, end_date):
    risk_free_rate_data = yf.download('^IRX', start=start_date, end=end_date)
    return risk_free_rate_data['Adj Close'] / 100  # Convert percentage to decimal

# Calculate daily returns
def calculate_returns(prices):
    return prices.pct_change().dropna()

# Build CAPM model
def calculate_CAPM(expected_market_return, risk_free_rate, beta):
    return risk_free_rate + beta * (expected_market_return - risk_free_rate)

# Main function
def main():
    # Define parameters
    ticker = 'NVDA'  # Replace with the desired stock ticker
    start_date = '2023-01-01'
    end_date = '2024-01-01'
    expected_market_return = 0.08  # Replace with the expected market return

    # Get stock data
    stock_prices = get_stock_data(ticker, start_date, end_date)

    # Get risk-free rate data
    risk_free_rate = get_risk_free_rate(start_date, end_date)

    # Calculate daily returns
    stock_returns = calculate_returns(stock_prices)
    market_returns = calculate_returns(yf.download('^NDX', start=start_date, end=end_date)['Adj Close'])

    # Calculate beta using linear regression
    beta, _, _, _, _ = linregress(market_returns.values, stock_returns.values)

    # Calculate expected return using CAPM
    expected_return = calculate_CAPM(expected_market_return, risk_free_rate.mean(), beta)

    print(f'Ticker: {ticker}')
    print(f'Beta: {beta:.4f}')
    print(f'Expected Return (CAPM): {expected_return:.4f}')

if __name__ == "__main__":
    main()