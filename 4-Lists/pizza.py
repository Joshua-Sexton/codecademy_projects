# Pizza shop list
#Make lists
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
#Length of toppings list
num_pizzas = len(toppings)
#Print ad
print("We sell "+str(num_pizzas)+" different kinds of pizza!")
#Create and print pizza list
pizzas = list(zip(prices, toppings))
print(pizzas)
#Sort pizzas
pizzas.sort()
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[0:3]
print(three_cheapest)
#Count $2 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
