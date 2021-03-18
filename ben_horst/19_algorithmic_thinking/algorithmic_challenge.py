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
            return
    print("Fruit not in list!")

check_if_fruit_in_list(fruit_list, 'grape')

# TODO Write the time complexity 
# The time complexity is O(n) or linear time


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

capitalize_meats_and_cheeses(meats, cheeses)

print(meats)
print(cheeses)
print()

# TODO Write the time complexity
# time complexity is O(n) or linear time

print("Question 3")
print()
# Write the time complexity for the function below, deli_meat_challenge
def deli_meat_challenge(meat, cheeses, sandwiches):
    sandwiches = {}
    for meat in meats:
        for cheese in cheeses:
            sandwiches.append(f'{meat} & {cheese}')
    return sandwiches

deli_meat_challenge('turkey', 'swiss', 'sandwiches')



# TODO Write the time complexity -
# the time complexity is O(n^2) or quadratic time

print("Question 4")
print()

'''
For the following question, you will be given an unsorted array that may contain duplicates. 
Your job is to write a function that returns true if there are duplicates and false if not.
Then write the time complexity of that function and think of if there are anyways you could have
made the algorithm more efficient? 
''' 

my_list = [5,2,3,4,5,8]
def contains_duplicates(my_list):
    for num1 in range(len(my_list)):
        for num2 in range(num1 + 1, len(my_list)):
            if my_list[num1] == my_list[num2]:
                return True
    return False


# TODO Write the time complexity
# Time complexity is O(n^2) - quadratic

## Bonus!
# Write a function that solves the problem, contains_duplicates in less time (i.e. lower time complexity).

print("Bonus:")

def contains_duplicates2(my_list):
    seen = {}

    for item in my_list:
        if item in seen:
            print("Yes, there is a duplicate!")
            return True
        else:
            seen[item] = item
            print("No, No duplicates!")
    return False
    

contains_duplicates2(my_list)

'''
def contains_duplicates_linear(my_list):
    seen = {}
    for item in my_list:
        if item in seen:
            return True
        seen[item] = item
    return False
'''

'''
Manav solution:


def contains_duplicates(my_list):
    seen = set()

    for item in my_list:
        if item in seen:
            return True
        else:
            seen[item] = item
    return False

# Manav's use of Maria's code using a list (dictionary {} is better)

def contains_duplicates(my_list):
    seen = []
    for item in my_list:
        if item in seen:
            return True
        else:
            seen.append(item)
    return False

'''