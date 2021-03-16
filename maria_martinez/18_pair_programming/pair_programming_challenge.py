'''
By: Maria and Dorian 
For this challenge, you will work in groups of 2 to 'pair program'
You'll need to work together to complete this challenge!
In general, 1 person should be typing, and the other should be leading what to code
But, it is always okay to swap roles or for the typing person to add their ideas too

-------------------------------------------------------------------


Your challenge: Make a bank account!
In this challenge, we want to make a bank account with 3 crucial functions
-create_account() - this function will initialize a bank account
-deposit() - add money to the account
-withdraw() - remove money from the account


PART 1: create_account()
This function should make a bank account!
The function does not need to take any arguments
The function should prompt the user using input() for username/password
The function should return a dictionary with 3 key/value pairs:
-username (string, should be what the user inputs)
-password (string, should be what the user inputs)
-balance (float, initialize this to 0)
'''

print('PART 1\n')
# TODO: define the create_account() function here and make sure it works
# HINT: make sure it works by doing something like my_account = create_account()
# Then print out my_account to see whether it has the correct info
def create_account():
    username = input('Please create username:\n')
    password = input('Please create password:\n')

    bankAccount = {
        "username": username,
        "password": password,
        "balance": 0.0
    }
    return bankAccount

my_account = create_account()
print(my_account)

# TODO: define password-protected withdraw_secure() and deposit_secure() functions
# HINT: there are tons of ways to do this correctly
# HINT: you can write any additional functions if you like

def validate(my_account):
    checkUserName = input('Please varify your username:\n')
    checkPassword = input('Please varify your password:\n')
    trueOrFalse = False
    
    if checkUserName == my_account["username"] and checkPassword == my_account["password"]:
        trueOrFalse = True

    return trueOrFalse

 

'''
PART 2: deposit()
This function should make a deposit to add money to the account
The function should take 2 arguments
-account (a dicionary representing a bank account, aka the output of create_account())
-amount (a float representing the amount to deposit)

The function does not need to return anything, but should increase the balance 
value by the appropriate amount

Test your function by making a few deposits to your account, 
then printing out your account
'''


print('PART 2\n')
# TODO define the deposit() function here and make sure it works
print('Before making a deposit validate your information:')

if validate(my_account) == False:
    print("\nInvalid username or password try again")
    validate(my_account) 

amount = float(input('\nPlease input amount you would like to deposit:\n'))
def deposit(my_account, amount):
    my_account['balance'] = amount

deposit(my_account,amount)
print(my_account)


'''
PART 3: withdraw()
This function should make a withdrawal to take money out of the account
The function should take 2 arguments:
-account (a dicionary representing a bank account, 
aka the output of create_account())
-amount (a float representing the amount to withdraw)

FIRST, the function should check whether there is enough 
money in the account to withdraw the requested amount
-If there is enough money, the function should decrease the balance 
value by the appropriate amount
-If there is not enough money, the function should print a message 
about the balance and tell the user there is not enough available 
to make that withdrawal

Test your function by making several withdrawals to your account
-try some you think will work AND some you think will 
not be allowed (more than the balance)
'''

print('PART 3\n')
# TODO define the withdraw() function here and make sure it works
print('Before making a withdraw validate your information:')

if validate(my_account) == False:
    print("\nInvalid username or password try again")
    validate(my_account)  

amountWithdraw = float(input('\nHow much would you like to withdraw?\n'))

def withdraw(account,amount):
    #using a conditional statement we are going to check if withdraw amount 
        #less then current amount in our bank account
    if account['balance'] >= amount:
        account['balance'] -= amount
        print(f"Your remaining balance is {account['balance']}")
    else:
        print("You do not have suffient funds.")
    

withdraw(my_account,amountWithdraw)
'''
BONUS QUESTION 4: Password-protect withdrawal and deposits
Make new deposit_secure() and withdraw_secure() functions 
that prompt the user for their username/password FIRST
Only let the transaction proceed if they enter the right info!
Otherwise, tell the user the info is wrong

Test out your new functions to make sure they accept correct 
info, and let the user know if the password/username is incorrect
'''

'''
i moved this to the top so i use one fucntion to validate the user information
'''