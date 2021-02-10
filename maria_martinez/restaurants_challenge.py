print("Challenge: Favourite Restaurants")

print()

print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. 
Go through the dictionary and print out the following 3 pieces of information about the restaurant: 
1. The latitude and longitude of Four Barrel Coffee 
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. 
3. The website of Four Barrel Coffee
'''


restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}

print(restaurant)

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
print()
print(f"lat: {restaurant['latitude']}, long: {restaurant['longitude']}\n")
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
print(f"Address:\n{restaurant['name']}\n{restaurant['address1']},\n{restaurant['city']}, {restaurant['state']} {restaurant['zip_code']}")
# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print(f"website: {restaurant['url']}")


print()

print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)
nycRestaurants = [{
    "name": "Lombardi's",
    "city": "New York",
    "state": "NY",
    "address1": "32 Spring St",
    "zip_code": "10012",
    "favDish": "pizza"
},{
    "name": "Joe's Shanghai",
    "city": "New York",
    "state": "NY",
    "address1": "46 Bowery",
    "zip_code": "10013",
    "favDish": "pork dumplings"
},{
    "name": "ABC Kitchen",
    "city": "New York",
    "state": "NY",
    "address1": "35 E 18th St",
    "zip_code": "10003",
    "favDish": "I have never been"
}]
# TODO: Print each dictionary
# for i in len(nycRestaurants):
n=len(nycRestaurants)
for i in range(0, n):
    print(f'{nycRestaurants[i]}\n')
print()

for i in range(0, n):
    print(nycRestaurants[i]['name'])
    print(nycRestaurants[i]['address1'])
    print(f"{nycRestaurants[i]['city']},{nycRestaurants[i]['state']} {nycRestaurants[i]['zip_code']}")
    print(f"My favorite dish: {nycRestaurants[i]['favDish']}")
    print()
# The dictionary for each restaurant should look something like this

'''
restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich" }
'''
print()

print("Question 3")
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there. 
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant
for i in range(0, n):
    nycRestaurants[i].pop('favDish')

print()
x=len(nycRestaurants)
for i in range(0, x):
    print(f'{nycRestaurants[i]}\n')

print("Question 4")
'''
Imagine that another one of your most favourite restaurants modified its address. 
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant 
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
# TODO: Print the updated dictionary.
nycRestaurants[0]['address']="Temporarly closed."
for i in range(0, x):
    print(f'{nycRestaurants[i]}\n')

