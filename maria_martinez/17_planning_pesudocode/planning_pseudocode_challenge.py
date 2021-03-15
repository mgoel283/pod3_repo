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
'''
I am going to create a list of dictionaries. I am doing this just in case I have to add more than one destination 
date shipped and weight. I can push the new dictonary of information into the exsisting list. 
to keep in one central location for the orders.
'''
orders=[
    {
        'destination': 'Los Angeles',
        'date_shipped': '03/10/2020',
        'weight': 10.08
    },
    {
        'destination': 'Los Angeles',
        'date_shipped': '03/10/2020',
        'weight': 10.08
    },
    {
        'destination': 'Los Angeles',
        'date_shipped': '03/10/2020',
        'weight': 10.08
    }
]

print('\nPART 1')


'''
2. Building the database

Now, let's put the orders all into a database togther (all the orders are stored in 1 variable). 

Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!). 

Print out the database to make sure all the info is in there. 

'''
'''I already did this by putting all my objects into a list in problem 1
'''
print('\nPART 2')


'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
'''
first we are going create the function called add_order()
we are going to ask the user to input the destination
we are going to ask the user when it was shipped
we are going to ask the user how much it was weighes 
and assign each one to the corresponding variable
then assign it into an object and push it into the original array
print the list to see if it worked
'''
def add_order():
    city = input('Please decalre what city the order was ship to:\n')
    date = input('Please input the date the order was shiped in this order month/day/year:\n')
    wt = float(input('Please input the weight of the item:\n'))

    obj = {
        'destination': city,
        'date_shipped':  date,
        'weight': wt 
    }

    orders.append(obj)
for i in range(0, len(orders)):
    print(f"{orders[i]}\n")

add_order()
print('\nPART 3')


'''
4. Define a function called complete_order() to mark a specific order in your database complete

This means you'll need a new piece of data inside the order that is True when the order is complete.

Test this out and print out your database to make sure it works!

HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
'''
first create the function
pass in the oder list and the index number that the user states has been completed
push in shipped with boolean set to true into the object  
print it out
'''
def complete_order(list, index):
    list[index]['shipped']=True
  
print('\nPART 4')
complete_order(orders, 1)
for i in range(0, len(orders)):
    print(f"{orders[i]}\n")

