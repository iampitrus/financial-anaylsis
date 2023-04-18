# Importing the Libraries
import sys
import plotly.graph_objects as go
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.cryptocurrencies import CryptoCurrencies


# Global Variables:
api_key = '4WDTBNMWPUFEEKN3'    #api key to database
app_name = "CURRENO"

# Creating the instances for CrptoCurrencies and ForeignExchange
av = ForeignExchange(key=api_key, output_format="pandas")
cc = CryptoCurrencies(key=api_key, output_format="pandas")

# BTC - Bitcoin, ETH - Ethereum, LTC - Litecoin, BNB - Binance coin, USDT - Tether
digital_currencies_codes = ["BTC","ETH","LTC","BNB","USDT"]
 
physical_currencies_codes = ["GBP", "USD", "EUR", "AUD", "JPY"]


## APP FUNCTIONS ##


# To get the current exchange rate of two physical currencies
def get_physical_currency_exchange_rate(from_currency, to_currency):
    print(f"Loading exchange rate for {from_currency}/{to_currency}...")
    fx, meta = av.get_currency_exchange_rate(from_currency, to_currency)
    # using loc to access data from a pandas dataframe
    rate = fx.loc["Realtime Currency Exchange Rate", "5. Exchange Rate"]
    from_currency_name = fx.loc["Realtime Currency Exchange Rate","2. From_Currency Name" ]
    to_currency_name = fx.loc["Realtime Currency Exchange Rate", "4. To_Currency Name"]
    time = fx.loc["Realtime Currency Exchange Rate", "6. Last Refreshed"]
    print(f"The current exchange Rate of {from_currency_name} to {to_currency_name} is {rate} as at {time}")
    reuse()

# To get the current exchange rate of two digital currencies
def get_crypto_currency_exchange_rate(from_crypto, to_crypto):
    print(f"Loading exchange rate for {from_crypto}/{to_crypto}...")
    cd, meta = cc.get_digital_currency_exchange_rate(from_crypto, to_crypto)
    rate = cd.loc["Realtime Currency Exchange Rate", "5. Exchange Rate"]
    from_crypto_name = cd.loc["Realtime Currency Exchange Rate","2. From_Currency Name" ]
    to_crypto_name = cd.loc["Realtime Currency Exchange Rate", "4. To_Currency Name"]
    time = cd.loc["Realtime Currency Exchange Rate", "6. Last Refreshed"]    
    print(f"The current exchange Rate of {from_crypto_name} to {to_crypto_name} is {rate} as at {time}")
    reuse()

# To plot the candlestick
def plot_candlestick(data, symbol, market, first_input, second_input):
    # Because they return different data type, then we use the data differently 
    # Check if market is empty
    if market == None:
        # For the physical currency pair chart
        trace = go.Candlestick(x=data.index,
                        open=data['1. open'],
                        high=data['2. high'],
                        low=data['3. low'],
                        close=data['4. close'])
        layout = go.Layout(title=f'{first_input}/{second_input} Daily Candlestick Chart')
    else:
        # For the Crypto currency chart
        trace = go.Candlestick(x=data.index,
                open=data[f'1a. open ({market})'],
                high=data[f'2a. high ({market})'],
                low=data[f'3a. low ({market})'],
                close=data[f'4a. close ({market})'])
        layout = go.Layout(title=f'{symbol} Daily Candlestick Chart in {market} market')
    fig = go.Figure(data=[trace], layout=layout)
    fig.show()

# To plot daily candlestick chart of a particular digital currency in a particular market
def plot_crypto_daily_candlestick_chart(symbol, market):
    print(f"Loading daily charts for {symbol} in {market} market...")
    
    # Returns  the daily historical time series for a digital currency (e.g., BTC) traded on a specific market (e.g., CNY/Chinese Yuan)
    crypt, crypt_meta = cc.get_digital_currency_daily(symbol, market)
    print("The Table:")
    print(crypt)
    print("Please check your Browser for result")
    plot_candlestick(data=crypt, symbol=first_input, market=second_input, first_input=None, second_input=None)
    plot_candlestick(data=crypt, symbol=first_input, market=second_input, first_input=None, second_input=None)
    reuse()

# Function to plot daily candlestick for physical currency pairs
def plot_physical_daily_candlestick_chart(first_input, second_input):
    print(f"Loading daily charts for {first_input}/{second_input}...")
    fx, meta = av.get_currency_exchange_daily(first_input, second_input)
    print("The Table:")
    print(fx)
    print("Please check your Browser for result")
    plot_candlestick(data=fx, symbol=None, market=None, first_input=first_input, second_input=second_input)
    plot_candlestick(data=fx, symbol=None, market=None, first_input=first_input, second_input=second_input)
    reuse()



## AUXILIARY FUNCTIONS
    
def physical_currencies():
    print("Choose An Option: ")
    print("1. Great Britain Pound")
    print("2. United States Dollar")
    print("3. Euro")
    print("4. Australian Dollar")
    print("5. Japanese Yen")

def digital_currencies():
    print("Choose An Option: ")
    print("1. BTC - Bitcoin")
    print("2. ETH - Ethereum")
    print("3. LTC - Litecoin")
    print("4. BNB - Binance coin")
    print("5. USDT - Tether")

def ask_pairs(type):

    # Creating global variables to be used in the menu function
    
    global first_input
    global second_input


    #Print the options of currency to select
    if type == "crypto":
        digital_currencies()
    else:
        physical_currencies()
    
    # Guide Messages
    # The type can either be Crypto or Physical depending on the user input
    print("Choose an option from 1-5")
    if type != "crypto chart":
        print(f"Enter the First {type} Currency")
    else:
        print("Choose the Crypto currency: ")
        digital_currencies()

    first_input = input("=> ")

    if type != "crypto chart":
        print("Choose an option from 1-5")
        print(f"Enter the Second {type} Currency")
    else:
        print("Choose the market type:")
        physical_currencies()
        
    second_input = input("=> ")

    # Check if correct input is passed in
    if not first_input in ["1","2","3","4","5"] or not second_input in ["1","2","3","4","5"]:
        if not first_input in ["1","2","3","4","5"]:
            print(f"\n\n{first_input} is not in the options")
        if not second_input in ["1","2","3","4","5"]:
            print(f"\n\n{second_input} is not in the options")
        print("You are expected to enter a number from 1-5")
        print("1. Try again")
        print("2. Return to main menu")
        print("3. Exit the app")
        # Give user option to retry, return to main menu and exit the app after incorrect input
        retry = input("=> ")
        if retry == "1":
            ask_pairs(type)
        elif retry == "2":
            menu()
        else:
            print("Thank you for using "+ app_name +"! Exiting.....")
            sys.exit()

    try:
        # Matching the chosen option to their codes
        first_input = int(first_input)
        second_input = int(second_input)
    except:
        return first_input, second_input
    else:
        if type == "crypto":
            first_input = digital_currencies_codes[first_input-1]
            second_input = digital_currencies_codes[second_input-1]
        elif type == "physical":
            first_input = physical_currencies_codes[first_input-1]
            second_input = physical_currencies_codes[second_input-1]
        # If the type is "crypto chart"
        else:
            #The first input is a crypto first_input 
            first_input = digital_currencies_codes[first_input-1]
            
            # The second input is the market
            second_input = physical_currencies_codes[second_input-1]
    
def reuse():
    print("Do you wish to use the app again?")
    answer = input("(yes or no)\n")
    if answer == "yes":
        menu()
    else:
        print("Exiting..")
        print("Thank you for using "+ app_name + "...")
        sys.exit()
    
def welcome_message():
    print("--------------------------------------")
    print("     WELCOME TO "+ app_name +"!       ")
    print("--------------------------------------\n")
    print("This is a prototype that enables users to get realtime exchange rates of currencies (digital and physical) and also plot the candlestick chart of currency pairs! ")
    print("You can also plot the candlestick charts for them also!\n\n")
    print("What do you want to do?")
    print("1. Get Exchange rate of Physical Currencies")
    print("2. Get Exchange rate of Digital Currencies")
    print("3. Plot Candlestick Chart of Physical Currencies")
    print("4. Plot Candlestick Chart of Digital Currencies")
    print("5. Exit the App")
    


## MENU FUNCTION

    
def menu():
    welcome_message()
    option = input("=> ")
    if option == "1":
        ask_pairs("physical")
        get_physical_currency_exchange_rate(from_currency=first_input, to_currency=second_input)
    elif option == "2":
        ask_pairs("crypto")
        get_crypto_currency_exchange_rate(from_crypto=first_input, to_crypto=second_input)
    elif option == "3":
        ask_pairs("physical")
        plot_physical_daily_candlestick_chart(first_input, second_input)
    elif option == "4":
        ask_pairs("crypto chart")
        plot_crypto_daily_candlestick_chart(first_input, second_input)
    elif option == "5":
        print("Thank you for using" +app_name +"! Exiting.....")
        sys.exit()
    else:
        print("Please enter a valid option!")
        menu()

menu()

'''
    CURRENO

    A python prototype use to get realtime trading data, this includes ploting the realtime candlestick charts
    and get the realtime exchange rates of currency pairs both Physical and Digital Currencies!!

    Built with 3 major libraries:
        - sys: inbuilt python library, it was used to exit the app here
        - alphavantage (https://www.alphavantage.co/): a python fintech library used to get realtime financial data by using their functions
        - plotly (https://plotly.com/): a Python library used to plot graph

    To run this app:
        - You need a good internet connection
        - You'll have to install alpha_vantage locally: pip install alpha-vantage
        - You'll have to install plotly library locally: pip install plotly==5.11.0
    
    Functions of the app:
        - get_physical_currency_exchange_rate (option 1): 
            User should be able to enter input for the options of currency type
            The current exchange rate of the selected currency pairs and the time is returned
        - get_digital_currency_exchange_rate (option 2):
            Similar to the option 1 but for digital (crypto) currency pairs
        - plot_physical_daily_candlestick_chart (option 3):
            User should be able to enter input of the chosen currency pair
            Returns  the daily historical time series for a digital currency
        (e.g., BTC) traded on a specific market (e.g., CNY/Chinese Yuan),
        refreshed daily at midnight (UTC).
        - plot_crypto_daily_candlestick_chart (option 4):
            Similar to option 3 but for digital currency pairs
            Also produce an interactive realtime trading candlestick charts on your browser,
            all these where possible with the help of the plotly library!
        
'''