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

print(f"The latitude is: {restaurant['latitude']}, and the longitude is:  {restaurant['longitude']}")

print(f"The address is: {restaurant['address1']}, {restaurant['city']}, {restaurant['state']}, {restaurant['zip_code']}")

print(f"The website is: {restaurant['url']}")

print()

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
# TODO: Write code to print the URL of the website of Four Barrel Coffee.

print()

print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)

fav_restaurant1 = {'name':'MaLa Project',
                    'address':'122 1st Avenue, New York, NY 10009',
                    'fav_dish':'Hot Pot'}

fav_restaurant2 = {'name':'Minetta Tavern',
                    'address':'113 MacDougal St, New York, NY 10012',
                    'fav_dish':'Steak'}

fav_restaurant3 = {'name':'Dr. Clark',
                    'address':'104 Bayard St, New York, NY 10013',
                    'fav_dish':'Risotto'}

# TODO: Print each dictionary

print(fav_restaurant1)
print(fav_restaurant2)
print(fav_restaurant3)

print()

print(f"My favorite restaurants are {fav_restaurant1['name']}, {fav_restaurant2['name']}, & {fav_restaurant3['name']}.")

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

fav_restaurant2.pop('fav_dish')

# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant

print(fav_restaurant2)

print()

print("Question 4")
'''
Imagine that another one of your most favourite restaurants modified its address. 
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant 

fav_restaurant1['address'] = '1 E 7th St, NY 10009'

# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary

print(f"The new address for {fav_restaurant1['name']} is {fav_restaurant1['address']}.")

print()

# TODO: Print the updated dictionary.
print(fav_restaurant1)

print()