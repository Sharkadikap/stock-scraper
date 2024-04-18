# What is this?
My personal stock scraper using yahoo finance API.<br>
It takes the value of the stock for the first day of January from year 2000 to 2024.<br>
It allows me to see the average % gain of the stock per year and make deductions for my stock investments.<br><br>
scrape.py takes the earliest yearly open value available (eg. 01/01/1990) to the latest yearly open value available.<br>
# How to use?
Edit the list from ticker_symbols.txt file to your desired ticker symbols or use ticker.py to get a list of your desired ticker symbols from a URL online.<br>
$ python ticker.py<br>
After running the code, the ticker_symbols.txt file will be overwritten.<br>
Next, run scrape.py to get google sheets version of the yearly open price of the stock. It will be output to the current folder.<br>
$ python scrape.py<br>
