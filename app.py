import streamlit as st
from services.stock_api import StockAPI
from analytics.indicators import add_ema, add_rsi
from utils.validators import Is_valid_company

st.set_page_config("Advanced Stock Market Dashboard", layout="wide")

@st.cache_resource
def get_client():
    return StockAPI()

client = get_client()

st.title("📊 Advanced Stock Market Dashboard")

company = st.text_input("Enter Company Name")

if company and Is_valid_company(company):
    symbols_df = client.search_symbols(company)

    if not symbols_df.empty:
        symbols = symbols_df["1. symbol"].tolist()
        selected = st.multiselect("Select Symbols", symbols)

        if selected:
            for sym in selected:
                st.subheader(sym)
                df = client.get_daily_prices(sym)

                df = add_ema(df, 20)
                df = add_rsi(df)

                st.dataframe(df.tail(5))

                fig = client.plot_candlestick(df)
                st.plotly_chart(fig, use_container_width=True)
