import yfinance as yf
import os

def fetch_and_save_stocks(tickers, start_date, end_date, data_folder="data/raw"):
    """
    Download historical data for multiple tickers and save each as a separate CSV.
    
    :param tickers: List of stock symbols (e.g. ['AAPL', 'MSFT', 'GOOGL']).
    :param start_date: Start date in 'YYYY-MM-DD' format.
    :param end_date: End date in 'YYYY-MM-DD' format.
    :param data_folder: Folder to save the CSV files. Default is 'data/raw'.
    """
    
    # Ensure the data folder exists
    os.makedirs(data_folder, exist_ok=True)
    
    for symbol in tickers:
        print(f"Fetching {symbol} from {start_date} to {end_date}...")
        df = yf.download(symbol, start=start_date, end=end_date)
        
        if not df.empty:
            filename = os.path.join(data_folder, f"{symbol}.csv")
            df.to_csv(filename)
            print(f"Saved {symbol} data to {filename}\n")
        else:
            print(f"No data returned for {symbol}\n")


if __name__ == "__main__":
    # Define a list of popular, high-volume US stocks (feel free to add/remove).
    tickers = [
        "AAPL",   # Apple
        "MSFT",   # Microsoft
        "GOOGL",  # Alphabet (Google)
        "AMZN",   # Amazon
        "TSLA",   # Tesla
        "META",   # Meta (Facebook)
        "NFLX",   # Netflix
        "NVDA",   # Nvidia
        "DIS",    # Walt Disney
        "BAC"     # Bank of America
    ]
    
    start_date = "2010-01-01"
    end_date = "2023-12-31"
    
    fetch_and_save_stocks(tickers, start_date, end_date)
