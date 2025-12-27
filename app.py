import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestRegressor

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Crypto AI Predictor", layout="wide")

# --- 1. DATA FETCHING FUNCTION (Binance API) ---
def get_live_data(symbol='BTCUSDT', interval='1d', limit=500):
    try:
        url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
        res = requests.get(url)
        data = res.json()
        df = pd.DataFrame(data, columns=[
            'Open_Time', 'Open', 'High', 'Low', 'Close', 'Volume', 
            'Close_Time', 'Quote_Asset_Volume', 'Number_of_Trades', 
            'Taker_Buy_Base_Asset_Volume', 'Taker_Buy_Quote_Asset_Volume', 'Ignore'
        ])
        df['Date'] = pd.to_datetime(df['Open_Time'], unit='ms')
        df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']].astype({
            'Open':float, 'High':float, 'Low':float, 'Close':float, 'Volume':float
        })
        return df
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

# --- FRONTEND UI DESIGN ---
st.title("💰 Real-Time Crypto Price AI Predictor")
st.markdown("""
    This dashboard uses **Live Data from Binance API** and a **Random Forest Machine Learning Model** to analyze market trends and predict future prices.
""")

# Sidebar for User Input
st.sidebar.header("Market Settings")
coin = st.sidebar.selectbox("Select Cryptocurrency", ("BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT"))
data_limit = st.sidebar.slider("Historical Data Days", 100, 1000, 500)

# Fetching Live Data
with st.spinner('Fetching live market data...'):
    df = get_live_data(coin, limit=data_limit)

if df is not None:
    # Display Current Metrics
    current_price = df['Close'].iloc[-1]
    prev_price = df['Close'].iloc[-2]
    price_diff = current_price - prev_price
    
    st.metric(label=f"Current {coin} Price", value=f"${current_price:,.2f}", delta=f"${price_diff:,.2f}")

    # --- 2. INTERACTIVE CANDLESTICK CHART ---
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['Open'], high=df['High'],
                    low=df['Low'], close=df['Close'], name="Market Data")])
    
    fig.update_layout(title=f"{coin} Price Analysis (Live)", yaxis_title="Price (USD)", template="plotly_dark", xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)

    # --- 3. MACHINE LEARNING (Random Forest) ---
    # Feature Engineering
    df['MA7'] = df['Close'].rolling(window=7).mean()
    df['MA21'] = df['Close'].rolling(window=21).mean()
    df['Target'] = df['Close'].shift(-1) # Predicting next day
    
    model_df = df.dropna()
    X = model_df[['Open', 'High', 'Low', 'Close', 'Volume', 'MA7', 'MA21']]
    y = model_df['Target']

    # Model Training
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Prediction Section
    st.divider()
    st.subheader("🔮 AI Price Forecast")
    
    if st.button('Generate Forecast for Tomorrow'):
        latest_features = df[['Open', 'High', 'Low', 'Close', 'Volume', 'MA7', 'MA21']].iloc[-1:].values
        prediction = model.predict(latest_features)[0]
        
        col1, col2 = st.columns(2)
        col1.write(f"**Today's Closing Price:** ${current_price:,.2f}")
        
        if prediction > current_price:
            col2.success(f"**Predicted Tomorrow:** ${prediction:,.2f} (Bullish Trend 📈)")
        else:
            col2.warning(f"**Predicted Tomorrow:** ${prediction:,.2f} (Bearish Trend 📉)")

# Footer
st.divider()
st.caption("Disclaimer: This tool is for educational purposes only and does not constitute financial advice.")