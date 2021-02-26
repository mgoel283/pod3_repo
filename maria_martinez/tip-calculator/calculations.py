#first I am going to create two variables 
 #then set them equal to the information from the user
print("~~~~~~~~~~Tip Calculator~~~~~~~~~~")
price = int(input('Please, enter total price:\n'))
percent = input('Please, enter tip percent amount :\n')
numOfPpl=int(input('Please, enther the total number of people in your party:\n'))

#Added this for loop to check if the user types in a percentage sign. if so then we remove the % sign
for i in range(len(percent)):
    if '%' in percent[i]:
        percent = percent[:i]

#calculate how much 10% is out of the price of bill
percentFromPrice = price * (int(percent)/100)
#add the ten percent to orginal bill
totalPrice = price + percentFromPrice
#divied the total price per person
totalPircePerPerson = round(totalPrice,2)/numOfPpl
#get the total tip person calculation
totalTipPerPerson = percentFromPrice/numOfPpl

#list out all the calculations for the user to see
print("~~~~~~~~~~Bill~~~~~~~~~~~~~~~~")
print(f'${price}')
print(f"~~~~~~Tip per person~~~~~~~~~~~~")
print(f'${round(totalTipPerPerson,2)}')
print(f"~~~~~~~Total per person~~~~~~~~~~")
print(f'${round(totalPircePerPerson,2)}')

