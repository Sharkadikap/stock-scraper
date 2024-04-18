import yfinance as yf
import pandas as pd

def fetch_yearly_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    # Resample data to keep only the first trading day of each year
    yearly_data = stock_data.resample('AS').first()
    return yearly_data[['Open']]

def save_to_excel(data, excel_filename):
    data['Date'] = data.index.strftime('%d-%m-%Y')  # Format 'Date' column
    data = data[['Date', 'Open']]  # Select only 'Date' and 'Open' columns
    data.to_excel(excel_filename, index=False, engine='openpyxl')

if __name__ == "__main__":
    # Request for user input for Ticker symbol
    stock_symbol = input("Ticker Symbol: ")

    # Fetch the full available data to determine the earliest start date
    full_data = yf.download(stock_symbol)
    earliest_start_date = full_data.index.min().strftime('%Y-%m-%d')

    # Fetch yearly stock data for 'Date' and 'Open' columns only, starting from the earliest date until 2024-01-01
    yearly_stock_data = fetch_yearly_stock_data(stock_symbol, earliest_start_date, '2025-01-01')

    if not yearly_stock_data.empty:
        # Save data to Excel file
        excel_filename = f'{stock_symbol}_yearly_open.xlsx'
        save_to_excel(yearly_stock_data, excel_filename)

        print(f"Data for {stock_symbol} has been saved to {excel_filename}.")
    else:
        print(f"No data available for the specified date range.")
