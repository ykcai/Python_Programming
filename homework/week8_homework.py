# Python Programming Week 8 Homework

'''
1. Create a function that takes a list and finds the integer which appears an odd number of times.

Examples
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1

find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5

find_odd([10]) ➞ 10

Notes: There will always only be one integer that appears an odd number of times.
'''


def find_odd(num_list):
    pass


print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
print(find_odd([10]))


'''
2. Return the Index of All Capital Letters
Create a function that takes a single string as argument and returns an ordered list containing the indexes of all capital letters in the string.

Examples
index_of_caps("eDaBiT") ➞ [1, 3, 5]

index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]

index_of_caps("determine") ➞ []

index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]

index_of_caps("sUn") ➞ [1]
Notes: Return an empty list if no uppercase letters are found in the string.
Special characters ($#@%) and numbers will be included in some test cases.
'''


def index_of_caps(word):
    pass


print(index_of_caps("eDaBiT"))
print(index_of_caps("eQuINoX"))
print(index_of_caps("determine"))
print(index_of_caps("STRIKE"))
print(index_of_caps("sUn"))

'''
3. Create a function that takes a list of integers and removes the smallest value.

Examples
remove_smallest([1, 2, 3, 4, 5] ) ➞ [2, 3, 4, 5]

remove_smallest([5, 3, 2, 1, 4]) ➞ [5, 3, 2, 4]

remove_smallest([2, 2, 1, 2, 1]) ➞ [2, 2, 2, 1]
Notes: Don't change the order of the left over items. If you get an empty list, return an empty list: [] ➞ []. If there are multiple items with the same value, remove item with lower index (3rd example).
'''


def remove_smallest(num_list):
    pass


print(remove_smallest([1, 2, 3, 4, 5]))
print(remove_smallest([5, 3, 2, 1, 4]))
print(remove_smallest([2, 2, 1, 2, 1]))
