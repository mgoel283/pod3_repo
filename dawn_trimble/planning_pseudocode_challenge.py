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
I will use a dictionary, so I can store the info about each order

Assign 3 separate orders to 3 separate variables
Order - destination , date of shipment , weight

Create 3 dictionaries with entries including destination, date shipped  and weight
'''

order_1 = {'destination':'Miami','date_shipped':'01/18/21','weight': 5.5 , 'shipped' : True}
order_2 = {'destination':'Puerto Rico', 'date_shipped': '10/06/20', 'weight': 4.5}
order_3 = {'destination':'New Orleans', 'date_shipped': '02/14/21', 'weight': 3.5, 'shipped' : True}

print('\nPART 1')


'''
2. Building the database

Now, let's put the orders all into a database togther (all the orders are stored in 1 variable). 

Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!). 

Print out the database to make sure all the info is in there. 

create a list that contains all the orders[]

'''

orders_database = [order_1, order_2, order_3]


print(orders_database)


'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
Define a function that adds new orders to to the database with destination, date shipped and weight
'''
'''create two new orders that will be appended to my database then create a function to add those orders
'''
order_4 = {'destination':'Portland', 'date_shipped': '02/18/21', 'weight': 6.5}
order_5 = {'destination':'Boston', 'date_shipped': '03/01/21', 'weight': 2.5}

def add_order(new):
    orders_database.append (new)
add_order(order_4)
add_order(order_5)
print(orders_database)


'''
4. Define a function called complete_order() to mark a specific order in your database complete

This means you'll need a new piece of data inside the order that is True when the order is complete.

Test this out and print out your database to make sure it works!

HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
def completed_list(database, order_index):
	database[order_index]['complete'] = True

#test to see if this works

completed_list(orders_database, 2)
completed_list(orders_database, 4)
print(orders_database)


