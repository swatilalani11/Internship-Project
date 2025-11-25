# Internship-Tasks

Task1 - Download Stock Data and Save as CSV: 
Steps : Takes stock symbol, date range and timeframe → downloads data from Yahoo Finance → cleans/resamples it → saves final data into a CSV file.
Work : This script fetches stock price data for the given period and timeframe, formats it, and stores it as a CSV file for easy analysis.

Task2 - Calculate Simple Moving Average (SMA): 
Steps : Creates a DataFrame of prices → loops through values → calculates 3-period Simple Moving Average → adds it as a new column. 
Work : This code calculates the 3-day Simple Moving Average (SMA) of price data and displays it alongside the original prices.

Task5 - Intraday Long Trade P/L Calculation: 
Steps: Downloads 1-minute stock data → selects entry and exit times → calculates daily profit/loss → summarizes overall P/L. 
Work: This script simulates an intraday long trade by buying at entry_time and selling at exit_time each day, then prints daily and total profit/loss.

Final Task1 - Stock Data Download API using yFinance:
Task Description: Create an API to download historical stock data using yFinance. POST accepts JSON input for symbol, dates, and timeframe; GET can use URL parameters for quick testing, returning OHLCV data in JSON.

Final Task2 - Simple Moving Average (SMA) API:
Task Description: Create an API to calculate Simple Moving Average (SMA) for a list of prices using a given window. Supports POST for JSON input and GET for quick browser testing.

Final Task3 - Weekly Expiry Date API for Indices: 
Task Description: Flask API that calculates the next weekly expiry date for indices like NIFTY, BANKNIFTY, and FINNIFTY. It accepts GET or POST requests with index and date parameters and returns the expiry date in JSON.

Final Task4 - Simple Flask API with / and /test Routes:
Task Description: Create a simple Flask API with two routes: / and /test. Both routes support GET and POST requests, return a JSON message, and echo any JSON data sent in POST requests.



