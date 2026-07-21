# Crypto Price Prediction – Real-Time ML Web App

A machine learning-powered web application that fetches live cryptocurrency data from the Binance API and predicts future price trends using a Random Forest Regressor. Built with Python, Streamlit, and Scikit-Learn.

## Overview

This project combines real-time data ingestion with a trained regression model to give users an interactive, easy-to-use interface for viewing and forecasting cryptocurrency price movements — no notebook or command line required.

## Features

- **Live data**: Pulls real-time cryptocurrency price data directly from the Binance API
- **Price prediction**: Uses a Random Forest Regressor to forecast short-term price trends
- **Interactive UI**: Built with Streamlit so users can select a coin, view live data, and see predictions in the browser
- **Visualizations**: Displays historical and predicted price trends on interactive charts

## Tech Stack

- **Language**: Python
- **ML Framework**: Scikit-Learn (Random Forest Regressor)
- **Web Framework**: Streamlit
- **Data Source**: Binance API
- **Data Handling**: Pandas, NumPy

## How It Works

1. The app fetches recent price data for a selected cryptocurrency from the Binance API
2. Data is cleaned and transformed into features suitable for the model
3. A Random Forest Regressor, trained on historical price data, generates a short-term price prediction
4. Results are displayed on an interactive Streamlit dashboard with charts comparing actual vs. predicted trends

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

Then open the local URL Streamlit provides in your browser, select a cryptocurrency, and view live data and predictions.

## Future Improvements

- Add support for more coins and longer prediction windows
- Experiment with additional models (XGBoost, LSTM) for comparison
- Add backtesting to evaluate prediction accuracy over time

## Author

Laiba Murtaza — [GitHub](https://github.com/LaibaMurtaza-21) | [LinkedIn](https://www.linkedin.com/in/laibamurtaza2109)
