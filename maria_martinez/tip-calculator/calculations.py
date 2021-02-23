#first I am going to create two variables 
 #then set them equal to the information from the user
print("~~~~~~~~~~Tip Calculator~~~~~~~~~~")
price = int(input('Please, enter total price:\n'))
percent = int(input('Please, enter tip %:\n'))
numOfPpl=int(input('Please, enther the total number of people in your party:\n'))

#calculate how much 10% is out of the price of bill
percentFromPrice = price * (percent/100)
#add the ten percent to orginal bill
totalPrice = price + percentFromPrice
#divied the total price per person
totalPircePerPerson = totalPrice/numOfPpl
#get the total tip person calculation
totalTipPerPerson = percentFromPrice/numOfPpl

#list out all the calculations for the user to see
print("~~~~~~~~~~Bill~~~~~~~~~~~~~~~~")
print(f'${price}')
print(f"~~~~~~~~~~Tip per person~~~~~~~~~~~~~~~~~")
print(f'${totalTipPerPerson}')
print(f"~~~~~~~~~~Total per person~~~~~~~~~~")
print(f'${totalPircePerPerson}')

