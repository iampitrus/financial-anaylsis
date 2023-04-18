# Libraries
import yfinance as yf
import matplotlib.pyplot as mpl
from dateutil import parser


# Global variables

# Company list: Telsa, Alibaba, Apple, Facebook(META), Amazon, Saudi Aramco, Google, Microsoft
companies = {1:"TSLA", 2:"BABA",3:"AAPL",4:"META",5:"AMZN",6:"2222.SR", 7:"GOOGL", 8:"MSFT"}

# Option to use for error handling
ticker_options = ["1","2","3","4","5","6","7","8"]



# Functions


# Function for basic stock information
def stock_lookup(ticker):
    print("Loading data, please wait....")
    stock = yf.Ticker(ticker)
    stock_info = stock.info
    print("Stock symbol: ", stock_info['symbol'])
    print("Company Name: ", stock_info['longName'])
    print("Current Price: $",stock_info['regularMarketPrice'])
    print(f"Market Cap:  ${stock_info['marketCap']:,}")

def stock_correlation_analysis(data):
    print("Loading data, Please wait...")

    # Extracting the data
    ticker1 = data[0]
    ticker2 = data[1]
    start = data[2]
    end = data[3]

    
    # Download historical stock data for two companies
    stock_data1 = yf.download(ticker1, start=start, end=end)
    stock_data2 = yf.download(ticker2, start=start, end=end)

    # Calculate the correlation between the two companies' closing prices
    correlation = stock_data1['Close'].corr(stock_data2['Close'])
    print(f'Correlation between {ticker1} and {ticker2} stock prices from {start} to {end} is {correlation}')

    # Plot the correlation between the two companies' closing prices
    mpl.scatter(stock_data1['Close'], stock_data2['Close'])
    mpl.xlabel(ticker1 + " Close Price")
    mpl.ylabel(ticker2 + " Close Price")
    mpl.title(f'Correlation between {ticker1} and {ticker2} stock prices from {start} to {end} is {correlation}')
    mpl.show()

# Function to calculate daily returns, mean returns and standard deviation of the returns
def returns(data):
    print("Loading data, Please wait....")
    # Extract data
    ticker = data[0]
    start = data[1]
    end = data[2]
    
    # Download historical stock data
    stock_data = yf.download(ticker, start, end)

    # Calculate the daily returns
    stock_data["return"] = stock_data["Adj Close"].pct_change()

    # Calculate the mean and standard deviation of the daily returns
    mean_return = stock_data["return"].mean()
    std_return = stock_data["return"].std()

    # Print the results
    print(f"Mean return for {ticker} from {start} to {end}: {mean_return:.4f}")
    print(f"Standard deviation of return for {ticker} from {start} to {end}: {std_return:.4f}")

# Function to plot the graph of revenue, expenses, and net income
# And Returns their individual mean values
def financial_statement(ticker):
    print("Loading Financial Statement data, please wait...")
    stock = yf.Ticker(ticker)
    # Get financial data for a specific stock
    financials = stock.financials
    # Transpose the pandas dataframe to be easily used in matplotlib
    financials = financials.transpose()
    
    # Extract from 2019 to 2022 of revenue, expenses and net income data
    expenses = financials['Total Expenses']
    revenue = financials['Total Revenue']
    net_income = financials["Net Income"]

    # Calculate their mean values
    mean_revenue = revenue.mean()
    mean_expense = expenses.mean()
    mean_net_income = net_income.mean()
    print(f"The Mean Revenue is: ${mean_revenue:,}")
    print(f"The Mean Expense is: ${mean_expense:,}")
    print(f"The Mean Income is: ${mean_net_income:,}")

    # Plot the data
    print("Ploting values...")
    mpl.plot(revenue, label='Revenue')
    mpl.plot(expenses, label='Expenses')
    mpl.plot(net_income, label= 'Net Income')

    # Add labels and legend
    mpl.xlabel('Year')
    mpl.ylabel('Amount')
    mpl.legend()

    # Show the plot
    mpl.show()


# Menu Function
def menu():
    print("\nWelcome to MY FINTECH PYTHON PROGRAM !\n")
    print("Please select an option from the menu:")
    print("1. Stock Lookup")
    print("2. Stock Correlation Analysis")
    print("3. Returns Analysis")
    print("4. Financial Statement Analysis")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

# Company list
def company_list():
    print("Select an option from 1-8:")
    print("1. Tesla")
    print("2. Alibaba")
    print("3. Apple")
    print("4. Facebook(Meta)")
    print("5. Amazon")
    print("6. Saudi Aramco")
    print("7. Alphabet. Inc (Google)")
    print("8. Microsoft")


# Defines the next course of action after wrong input
def what_next(error_type):
    print("Invalid input!")
    print("1. Retry")
    print("2. Return to menu")
    print("3. Exit")
    option = input("")

    # Check the error type
    if option == "1":
        if error_type == "ticker_value":
            company_list()
            print("Please enter a numeric value in the range of 1 - 8")
            selected_company = input("Choose a company: ")
            return selected_company
        else:
            print("Please enter a valid format(YYYY-MM-DD), For example: 2020-01-10")
            date = input("Re-enter date: ")
            date = check_date(date)
            return date

    elif option == "2":
        main_menu()
    else:
        quit("Thank you for using the FinTech Python Program. Exiting...")


# Function to check ticker input and return the ticker
def check_ticker(selected_company):
    while not selected_company in ticker_options:
        selected_company = what_next("ticker_value")
    selected_company = int(selected_company)
    # Assign the ticker for the company selected
    ticker = companies[selected_company]
    return ticker


# Function to check if format matches the date 
def check_date(value):
    
    response = True
    # using try-except to check for truth value
    while response:
        try:
            bool(parser.parse(value))
        except ValueError:
            print(value + " is an incorrect input format")
            value = what_next("date_value")
        else:
            response = False
            return value

# Function to take user input, the option parameter is use to know the selected option
def evaluate (option):
    
    if option != 2:
        company_list()
        selected_company = input("Choose a company: ")
        # Check if a number in the options is passed in and number passed
        ticker = check_ticker(selected_company)

    else:
        # Input for the first ticker
        company_list()
        first_company = input("Choose the first company: ")
        ticker1 = check_ticker(first_company)

        # Input for the second ticker
        company_list()
        second_company = input("Choose the second company: ")
        ticker2 = check_ticker(second_company)
        
    if option == 2 or option == 3 :
        print("Enter date in this format: YYYY-MM-DD. Use hyphens to seperate them")
        start_date = input("Enter start date: ")
        
        # Check the data passed in as date
        start_date = check_date(start_date)

        end_date = input("Enter end date: ")
        # Check the data passed in as date
        end_date = check_date(end_date)



    # Define what is returned based on the options
    if option == 1 or option == 4:
        return ticker

    if option == 2:
        return ticker1, ticker2, start_date, end_date

    if option == 3:
        return ticker, start_date, end_date

        
# Menu Function

def main_menu():
    while True:
        choice = menu()
        if choice == '1':
            print("This function returns realtime stock information of chosen company")
            choice = int(choice)
            stock_lookup(evaluate(choice))
        elif choice == '2':
            print("This function calculates the stock correlation between two companies and plots a graph")
            choice = int(choice)
            stock_correlation_analysis(evaluate(choice))
        elif choice == '3':
            print("This function calculates returns, mean return and standard deviation for the return of chosen company to be used for anaylsis")
            choice = int(choice)
            returns(evaluate(choice))
        elif choice == "4":
            print("This function plots graph for revenue, expense and net income, It also calculates the mean revenue, expense and net income over the space of 3 years for chosen company")
            choice = int(choice)
            financial_statement(evaluate(choice))
        elif choice == '5':
            print("Thank you for using the FinTech Python Program. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        cont = input("Do you want to return to the menu? (y/n)")
        if cont.lower() == 'n':
            print("Thank you for using My FinTech Python Program. Exiting...")
            break
    

# Run main_menu function only when script is ran directly
if __name__ == "__main__":
    main_menu()



# MY FINTECH PYTHON PROGRAM
    # A Program used to get realtime financial data of companies, which can be used for analysis, the retrieves these data from Yahoo Finance.
    # The program also aids visualization of these data by ploting them on graph
    # App Thoroughly checks input passed in for validation


# REQUIREMENTS TO RUN PROGRAM:
    # Must have Python installed. visit (https://www.python.org)
    # Install yfinance using the command pip install yfinance . Website - https://finance.yahoo.com
    # Install matplotlib using the command pip install matplotlib . Website - https://matplotlib.org

# LIBRARIES:
    # yfinance: External library Used to get realtime financial data of companies 
    # matplotlib: External Library Used for data visualization, to plot graphs
    # dateutil: Inbuilt library, was used to validate the date input passed in check_date() function

# APP FUNCTIONS:
    # STOCK LOOKUP: Function returns the current stock price, market cap, full name and stock symbol of a company
    # STOCK CORRELATION ANALYSIS: Function calculates the stock correlation between two companies over a specified time range
    # RETURNS: Function to calculate daily returns, mean returns and standard deviation of the returns for a company over a specified time range
    # FINANCIAL STATEMENT ANALYSIS: Function to get the revenue, expense and net-income for a particular company from 2019 to 2022 and plot these values on a graph for visualisation. It also calculates the mean revenue, expense and net income. 
    