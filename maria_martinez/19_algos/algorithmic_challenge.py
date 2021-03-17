# Algorithmic Challenge
import time

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


# TODO Write the time complexity
# O(n) + O(1) = O(n) 

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
#O(n) + O(n)= O(2n)= O(n) (ignore the 2)

print("Question 3")
print()
# Write the time complexity for the function below, deli_meat_challenge
def deli_meat_challenge(meat, cheeses, sandwiches):
    for meat in meats:
        for cheese in cheeses:
            sandwiches.append(f'{meat} & {cheese}')
    return sandwiches

# TODO Write the time complexity
# O(n)*O(n)=O(n^2)


print("Question 4")
print()

'''
For the following question, you will be given an unsorted array that may contain duplicates. 
Your job is to write a function that returns true if there are duplicates and false if not.
Then write the time complexity of that function and think of if there are anyways you could have
made the algorithm more efficient? 
''' 
#create a new array and push in the elements inside the array and if the element is already inside the array we can 
#just contiune to the next element

def contains_duplicates(my_list):
    newArr = []
    trueOrFalse = True
    for i in range(0,len(my_list)):
        if my_list[i] not in newArr:
           newArr.append(my_list[i])
        else:
            trueOrFalse = False
    return trueOrFalse

#this test case will print true
startTime = time.time()
my_list = [5,2,3,4,8]
duplicates = contains_duplicates(my_list)
print(duplicates)
print(time.time()- startTime)#this will be subtract the end time with the start time and return the value in seconds

#this test case will print false
startTime = time.time()
my_list = [5,2,3,4,5,8]
duplicates = contains_duplicates(my_list)
print(duplicates)
print(time.time()- startTime)#this will be subtract the end time with the start time and return the value in seconds
# TODO Write the time complexity
# O(n)+O(1) = O(n) 

## Bonus!
# Write a function that solves the problem, contains_duplicates in less time (i.e. lower time complexity).

#Manav version is faster
def contains_duplicates_linear(my_list):
    seen = {}
    for item in my_list:
        if item in seen:
            return True
        seen[item] = item
    return False

#this test case will print true
startTime = time.time()
my_list = [5,2,3,4,8]
duplicates = contains_duplicates(my_list)
print(duplicates)
print(time.time()- startTime)#this will be subtract the end time with the start time and return the value in seconds

#this test case will print false
startTime = time.time()
my_list = [5,2,3,4,5,8]
duplicates = contains_duplicates(my_list)
print(duplicates)
print(time.time()- startTime)#this will be subtract the end time with the start time and return the value in seconds