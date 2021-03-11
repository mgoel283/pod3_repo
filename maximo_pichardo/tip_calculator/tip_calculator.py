cost_of_food= input('how much the food cost')
number_of_people= input('How many people')
pct_of_tip= input('How much the cost of tip')
print(cost_of_food, number_of_people, pct_of_tip)
#sales tax= .10
#pct of tip= .18

#calculate 10% sales tax to the total cost of food
tax= .1 * cost_of_food
#add 18% in tip to cost of food plus sales tax
tip= .18 * cost_of_food + tax

total_bill= cost_of_food + tax + tip

#cost per person
total_bill / number_of_people