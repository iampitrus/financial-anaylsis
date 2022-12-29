import yfinance as yf
import matplotlib.pyplot as plt


# Get current stock Quote
def get_stock_quote(stock, company_name):
  info = stock.info
  print(f"The current stock quote of {company_name} is ${info['regularMarketPrice']}")

# Function to plot stock prices over time
def plot_stock_prices(stock, start_date, end_date, company_name):
  history = stock.history(start=start_date, end=end_date)
  history.plot(y="Close")
  plt.xlabel("Date")
  plt.ylabel("Price")
  plt.title(f"{company_name} Stock Prices")
  plt.show()

# Function to calculate ROI
def calculate_roi(stock, start_date, end_date, company_name):
  history = stock.history(start=start_date, end=end_date)
  # Since rio is ((final value of investment - initail value of investment) / initial value of investment) * 100
  # history["Close"][-1] selects the last/final value of investment with respect to the chosen "end date"
  # history["Close"][0] selects the first/intial value of investment with respect to the chosen "start date"
  roi = ((history["Close"][-1] - history["Close"][0]) / history["Close"][0])*100
  print(f"ROI for {company_name} between {start_date} and {end_date} is {roi:.2f}%")

# Function to get total Revenue
def get_total_revenue(stock, company_name):
  revenue = stock.info['totalRevenue']
  # On the returned value of revenue, place a comma in between every 3 digits
  print(f"Total Revenue of {company_name} is: ${revenue:,}")

def choose_company_option():
  print("Choose a company: ")
  print("\n1. Apple") 
  print("2. Microsoft") 
  print("3. Meta") 
  print("4. Google")
  print("5. Amazon")
  print("6. Netflix")
  print("7. Tesla")
  print("8. Visa")
  print("9. Nvidia")
  print("10. Chevron")


# Define main menu function
def main_menu():
  company_chosen = None

  while True:
    text = "   again" if company_chosen else "   to    M y F i n T e c h A p p!"
    print("------------------------------------------------------")
    print(f"    W E L C O M E {text.upper()}    ")
    print("------------------------------------------------------")
    print("\n!!!  Ensure there is a good internet connection before proceeding   !!!\n".upper())
    print("Please select an option:")
    print("1. Get stock quote")
    print("2. Plot stock prices")
    print("3. Calculate Return on Investment (ROI)")
    print("4. Get Total Revenue")
    print("5. Exit")

    selection = input("> ")

    main_options = ["1","2","3","4"]
    # Check if option 1 - 4 is selected
    if selection in main_options:
      # Check if I've use the app before
      if company_chosen is not None:
        print(f"Do you wish to use {company_fullName} again? \n")
        reuse = input("Yes or No: \n")
        # If user wants to choose a new company
        if reuse.lower() == 'no':
          # Ask for input and convert input to integer for easy accessibility
          choose_company_option()
          company_chosen = int(input("> "))
      else:
        choose_company_option()
        company_chosen = int(input("> "))

      # Dictionary of company tickers, which will be queried to yfinance
      company_tickers = {
        1: "AAPL",  # Apple
        2: "MSFT",  # Microsoft
        3: "META",  # Meta
        4: "GOOG",  # Google
        5: "AMZN",  # Amazon
        6: "NFLX",  # Netflix
        7: "TSLA",  # Tesla
        8: "V",     # Visa
        9: "NVDA",  # Nvidia
        10: "CVX"   # Chevron
      }

      # Check if user entered a valid option
      if company_chosen in company_tickers:
        # Select the ticker from company_tickers dictionary
        symbol = company_tickers[company_chosen]
        stock = yf.Ticker(symbol)
        # Get company full name
        company_fullName = stock.info['longName']
      else:
        print("Invalid Selection! ")

      # If the First option is selected
      if selection == "1":
        get_stock_quote(stock, company_fullName)
      
      # If the Second option is selected
      elif selection == "2":
        print("Use this format for date: year-month-day, for example 2022-10-12")
        start = input("Enter a start date: ")
        end = input("Enter a end date: ")
        plot_stock_prices(stock, start, end, company_fullName)

      # If the Third option is selected
      elif selection == "3":
        print("Enter a time period for the ROI calculation of")
        print("Use this format for date: year-month-day, for example 2022-10-12")
        start = input("Enter a start date: ")
        end = input("Enter a end date: ")
        calculate_roi(stock, start, end, company_fullName)

      # If the Fourth option is selected
      else:
        get_total_revenue(stock, company_fullName)
        
    elif selection == "5":
      break

    # If a wrong input is passed in
    else:
      print("Invalid selection, choose from the options provided!")

# Run main menu function
main_menu()