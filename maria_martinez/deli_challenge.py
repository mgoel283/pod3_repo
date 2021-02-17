
print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()
for i in range(len(meats)):
    meats[i]=meats[i].capitalize()
print(meats)
for i in range(len(cheeses)):
    cheeses[i]=cheeses[i].capitalize()
print(cheeses)

print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list
sandwiches = []
for i in range(len(meats)):
    for j in range(len(cheeses)):
        sandwiches.append(meats[i]+' '+cheeses[j])

print(sandwiches)

print('Question 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
# TODO: Loop over the sandwiches list.
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'
print(meats)
print(cheeses)
meatsOrder=input("Please select meat option:\n").capitalize()
cheeseOrder=input("Please select a cheese option:\n").capitalize()

orderCombo=meatsOrder+' '+cheeseOrder

if orderCombo in sandwiches:
    print(f"Great choice! 1 {meatsOrder} & {cheeseOrder} coming right up!")
else: 
    print("not an option")