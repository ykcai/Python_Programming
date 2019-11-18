# Python Programming Week 9 Homework

# Question 1
# Area of a Triangle
# Write a function that takes the base and height of a triangle and return its area.


def tri_area(width, heigh):
    pass


print(tri_area(3, 2))
print(tri_area(7, 4))
print(tri_area(10, 10))

# Question 2
# The Farm Problem
# You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm.
# Return the total number of legs on your farm.


def animals(chickent, cow, pigs):
    pass


print(animals(2, 3, 5))
print(animals(1, 2, 3))
print(animals(5, 2, 8))

# Question 3
'''
If you get this one right, I will let you skip the test!
'''
# Calculate the Profit
# You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product.
# You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars),
# and the starting inventory. Return the total profit made, rounded to the nearest dollar.
# Assume all of the inventory has been sold.


def profit(input_dict):
    print(input_dict['cost_price'])


print(profit({
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
}))
# print(profit({
#     "cost_price": 225.89,
#     "sell_price": 550.00,
#     "inventory": 100
# }))
# print(profit({
#     "cost_price": 2.77,
#     "sell_price": 7.95,
#     "inventory": 8500
# }))
