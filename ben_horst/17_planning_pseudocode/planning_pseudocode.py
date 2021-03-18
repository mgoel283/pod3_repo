'''
Planning & pseudocode challenge!
For each piece here, write out the pseudocode as comments FIRST, then write your code!
At many points, you'll have to choose between using a list vs. dictionary. Justify your choices!
'''


'''
1. Shipping
You are building a system to handle shipping orders. Each order should have 3 pieces of information:
-destination (string) (for the purposes of this challenge this can be any place, no need to make a full address)
-date_shipped (string)
-weight (float) (how many pounds the package is)
Will you choose to make each shipping order as a dictionary or list? Why?
Assign 3 separate orders to 3 separate variables
'''
print('\nPART 1')

# using a dictionary to include all 3 variables
order_1 = {'destination': 'Philly', 'date shipped': '2/15/21', 'weight': 20}
order_2 = {'destination': 'NYC', 'date shipped': '2/28/21', 'weight': 15}
order_3 = {'destination': 'Boston', 'date shipped': '3/1/21', 'weight': 10}

print(order_1)
print()
print(order_2)
print()
print(order_3)
print()

'''
2. Building the database
Now, let's put the orders all into a database togther (all the orders are stored in 1 variable). 
Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!). 
Print out the database to make sure all the info is in there. 
'''
print('\nPART 2')

# this puts all of the orders into one list
order_database = [order_1, order_2, order_3]
print(order_database)

print()

'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')

# creating the two additional orders
order_4 = {'destination': 'Baltimore', 'date shipped': '3/15/21', 'weight': 25}
order_5 = {'destination': 'Chicago', 'date shipped': '1/15/21', 'weight': 20}

# defined the function that has two variables - order & database

def add_order_list(database, order):
    database.append(order) #appending the order to the database


# using the new function with the two variables - the database variable defined earlier & the 2x new orders I just made
add_order_list(order_database, order_4)
add_order_list(order_database, order_5)

print(order_database)

'''
4. Define a function called complete_order() to mark a specific order in your database complete
This means you'll need a new piece of data inside the order that is True when the order is complete.
Test this out and print out your database to make sure it works!
HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
print('\nPART 4')

def complete_order(database, order_num):
    database[order_num]['complete'] = True

# test it out 
complete_order(order_database, 1)
complete_order(order_database, 3)

# print out to check it
print(order_database)