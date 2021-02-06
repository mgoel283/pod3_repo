print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
name=input("Please enter your first name:\n")
# TODO: Write code to ask the client his savings and save it to another variable.
clientSaving=input(f"How much do you have in your savings {name}:\n")
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.\n")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
shares=''
pricePerShare=''
if stock == "amzn":
    shares=amazon/int(clientSaving)
    pricePerShare=amazon
elif stock=='aapl':
    shares=apple/int(clientSaving)
    pricePerShare=apple
elif stock=='fb':
    shares=fb/int(clientSaving)
    pricePerShare=fb
elif stock=='goog':
    shares=google/int(clientSaving)
    pricePerShare=google
elif stock=='msft':
    shares=msft/int(clientSaving)
    pricePerShare=msft
else:
    print("invalid entry")

'''
Your code should look like this:
if stock == "amzn":
    ...
elif ...
else ...
'''

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:
print(f"{name} has ${clientSaving} in savings and they can buy {shares} shares of {stock} at the current price of ${pricePerShare}.")
# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print()