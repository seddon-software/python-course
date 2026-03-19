import yfinance as yf

def get_ibm_price():
    """Fetch the current share price of IBM"""
    try:
        ibm = yf.Ticker("IBM")
        data = ibm.history(period="1d")
        current_price = data['Close'].iloc[-1]
        print(f"IBM Current Price: ${current_price:.2f}")
        return current_price
    except Exception as e:
        print(f"Error fetching IBM price: {e}")
        return None

if __name__ == "__main__":
    get_ibm_price()