# Crypto Price Prediction – Real-Time ML Web App

A real-time cryptocurrency price prediction web application built with **Python**, **Streamlit**, **Plotly**, and **Scikit-Learn**. The app fetches live market data from the Binance API and uses a Random Forest Regressor to forecast the next day's closing price.

## Overview

This project combines live data ingestion, interactive visualization, and machine learning to give users a working dashboard for tracking cryptocurrency prices and generating short-term forecasts — all through a simple web interface, no notebook required.

## Features

- **Live data**: Fetches real-time OHLCV (Open, High, Low, Close, Volume) data directly from the Binance API
- **Multi-coin support**: Choose between BTC, ETH, BNB, and SOL via a dropdown
- **Interactive candlestick chart**: Built with Plotly for visual price analysis, styled with a dark theme
- **Feature engineering**: Calculates 7-day (MA7) and 21-day (MA21) moving averages as model inputs
- **Next-day price forecast**: A Random Forest Regressor trained on live data predicts tomorrow's closing price on demand
- **Live metrics**: Displays current price and price change at a glance
- **Trend signal**: Flags the forecast as bullish or bearish relative to the current price

## Tech Stack

- **Language**: Python
- **Web Framework**: Streamlit
- **ML Framework**: Scikit-Learn (Random Forest Regressor)
- **Visualization**: Plotly (candlestick charts)
- **Data Source**: Binance API
- **Data Handling**: Pandas, NumPy

## How It Works

1. The app fetches recent OHLCV data for the selected cryptocurrency from the Binance API
2. Data is cleaned, converted to the correct types, and indexed by date
3. Moving averages (MA7, MA21) are calculated as engineered features
4. A Random Forest Regressor is trained on the processed data, using the next day's closing price as the target
5. On clicking "Generate Forecast," the model predicts tomorrow's closing price using the most recent data point
6. Results are displayed with a bullish/bearish signal based on whether the prediction is above or below the current price

## Installation

```bash
git clone https://github.com/LaibaMurtaza-21/Crypto-Project-Real-Time-.git
cd Crypto-Project-Real-Time-
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

Then open the local URL Streamlit provides, select a cryptocurrency and historical data range from the sidebar, and click **"Generate Forecast for Tomorrow"** to see the AI prediction.

## Disclaimer

This tool is for educational purposes only and does not constitute financial advice.

## Future Improvements

- Backtest the model's prediction accuracy over time
- Experiment with additional models (XGBoost, LSTM) for comparison
- Add more technical indicators (RSI, MACD) as features
- Extend forecasting beyond a single day ahead

## Author

Laiba Murtaza — [GitHub](https://github.com/LaibaMurtaza-21) | [LinkedIn](https://www.linkedin.com/in/laibamurtaza2109)
