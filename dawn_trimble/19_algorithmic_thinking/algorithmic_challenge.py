# Algorithmic Challenge


print("Question 1")
print()

fruit_list = ["apple", "orange", "banana", "pear", "grape", "pineapple"]
fruit = "pear"
# Write the time complexity for the function below, check_if_fruit_in_list

def check_if_fruit_in_list(my_list, fruit):
    for fruit_item in my_list:
        if fruit_item == fruit:
            print("Fruit in list!")
    print("Fruit not in list!")


print('O(n) Linear')


# For Questions 2 and 3, we are going to look at the time complexities for the previous deli meats challenge

meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

print("Question 2")
print()
# Write the time complexity for the function below, capitalize_meats_and_cheeses
def capitalize_meats_and_cheeses(meats, cheeses):
    for i in range(len(meats)):
        meats[i] = meats[i].capitalize()

    for i in range(len(cheeses)):
        cheeses[i] = cheeses[i].capitalize()

# TODO Write the time complexity
print('O(n) linear as well')


print("Question 3")
print()
# Write the time complexity for the function below, deli_meat_challenge
def deli_meat_challenge(meat, cheeses, sandwiches):
    for meat in meats:
        for cheese in cheeses:
            sandwiches.append(f'{meat} & {cheese}')
    return sandwiches

# TODO Write the time complexity

print("quadratic O(n^2)")



print("Question 4")
print()

'''
For the following question, you will be given an unsorted array that may contain duplicates. 
Your job is to write a function that returns true if there are duplicates and false if not.
Then write the time complexity of that function and think of if there are anyways you could have
made the algorithm more efficient? 
''' 

my_list = [2,5,3,4,5,8]
def contains_duplicates(my_list):
    for item1 in range(len(my_list)):
        for item2 in range(item1 + 1,len(my_list)):
            if my_list[item1] == my_list[item2]:
                return True
    return False


# TODO Write the time complexity
print('Time complexity is O(n^2)')

## Bonus!
# Write a function that solves the problem, contains_duplicates in less time (i.e. lower time complexity).

def contains_dupes(my_list):
    seen = {}
    for item in my_list:
        if item in seen:
            return True
        seen[item] = item
    return False
