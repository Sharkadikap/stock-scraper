import yfinance as yf
import pandas as pd

def fetch_yearly_stock_data(symbol, start_date, end_date):
    try:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        # Resample data to keep only the first trading day of each year
        yearly_data = stock_data.resample('YS').first()
        return yearly_data[['Open']], None
    except Exception as e:
        print(f"Failed to fetch data for {symbol}: {e}")
        return pd.DataFrame(), symbol  # Return an empty DataFrame and the failed symbol

def save_to_excel(data, excel_filename):
    data['Date'] = data.index.strftime('%d-%m-%Y')  # Format 'Date' column
    data = data[['Date', 'Open']]  # Select only 'Date' and 'Open' columns
    data.to_excel(excel_filename, index=False, engine='openpyxl')

if __name__ == "__main__":
    # Read ticker symbols from the text file
    with open('ticker_symbols.txt', 'r') as file:
        ticker_symbols = file.read().splitlines()

    failed_symbols = []
    for stock_symbol in ticker_symbols:
        # Fetch the full available data to determine the earliest start date
        full_data = yf.download(stock_symbol)
        
        if isinstance(full_data, pd.DataFrame) and not full_data.empty:
            earliest_start_date = full_data.index.min().strftime('%Y-%m-%d')
            # Fetch yearly stock data for 'Date' and 'Open' columns only, starting from the earliest date until 2024-01-01
            yearly_stock_data, failed_symbol = fetch_yearly_stock_data(stock_symbol, earliest_start_date, '2025-01-01')

            if not yearly_stock_data.empty:
                # Save data to Excel file
                excel_filename = f'{stock_symbol}_yearly_open.xlsx'
                save_to_excel(yearly_stock_data, excel_filename)

                print(f"Data for {stock_symbol} has been saved to {excel_filename}.")
            else:
                print(f"No data available for {stock_symbol} for the specified date range.")
                if failed_symbol:
                    failed_symbols.append(failed_symbol)
        else:
            print(f"Failed to fetch data for {stock_symbol}.")
            failed_symbols.append(stock_symbol)
    
    if failed_symbols:
        print("The following ticker symbols failed to be fetched:")
        for symbol in failed_symbols:
            print(symbol)
