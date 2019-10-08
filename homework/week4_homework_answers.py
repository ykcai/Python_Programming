# Python Programming Week 4 Homework Answers

# Question 0:
# --------------------------------Code between the lines!--------------------------------


def less_than_five(input_list):
    '''
    ( remember, index starts with 0, Hint: for loop )
    # Take a list, say for example this one:
    # my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # and write a function that prints out all the elements of the list that are less than 5.
    '''
    for num in input_list:
        if num < 5:
            print(num)


my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_five(my_list)

# ---------------------------------------------------------------------------------------

# Question 1:
# --------------------------------Code between the lines!--------------------------------


def divide_seven_and_five():
    '''
    # Write a function which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    # between 2000 and 3200 (both included).
    # The numbers obtained should be printed in a comma-separated sequence on a single line.
    # Hints: Consider use range(start, end) method
    '''
    # Write your code here
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            print(i)


divide_seven_and_five()
# ---------------------------------------------------------------------------------------

# Question 2.
# Instead of using math multiply operation, please make use of range to do the multiplication.
# Hint: rang(start, end, step)  step is the increment to add. By default, it is 1.
# Examples:
# Input : n = 2, m = 3
# Output : 6

# Input : n = 3, m = 4
# Output : 12
# --------------------------------Code between the lines!--------------------------------
def multiplication(n, m):
    result = 0
    for i in range(0, m):
        result = result + n
    print(result)
    return result
    
multiplication(2,3)
multiplication(3,4)

# ---------------------------------------------------------------------------------------
