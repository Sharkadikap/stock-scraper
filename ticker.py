import pandas as pd
import requests

def get_sp500_ticker_symbols(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        tables = pd.read_html(response.text)
        for table in tables:
            if 'Symbol' in table.columns:
                return table['Symbol'].tolist()
        print("No table with 'Symbol' column found on the webpage.")
        return []
    except Exception as e:
        print(f"Failed to fetch data from webpage: {e}")
        return []

def save_ticker_symbols_to_txt(ticker_symbols, filename):
    with open(filename, 'w') as file:
        for symbol in ticker_symbols:
            file.write(symbol + '\n')
    print(f"Ticker symbols saved to {filename}.")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    ticker_symbols = get_sp500_ticker_symbols(url)
    if ticker_symbols:
        save_ticker_symbols_to_txt(ticker_symbols, "ticker_symbols.txt")
    else:
        print("No ticker symbols found.")
