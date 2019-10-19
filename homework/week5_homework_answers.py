# Python Programming Week 5 Homework Answers
# 1.


def lesser_of_two_evens(a, b):
    '''
    LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
    lesser_of_two_evens(2,4) --> 2
    lesser_of_two_evens(2,5) --> 5
    '''
    # Write your code here
    # --------------------------------Code between the lines!--------------------------------
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)
    # ---------------------------------------------------------------------------------------


# Check
print(lesser_of_two_evens(2, 4))
# Check
print(lesser_of_two_evens(2, 5))

# 2.


def animal_crackers(text):
    '''
    ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
    animal_crackers('Levelheaded Llama') --> True
    animal_crackers('Crazy Kangaroo') --> False
    '''
    # Write your code here
    # --------------------------------Code between the lines!--------------------------------
    word_list = text.split(" ")
    print(word_list)
    return word_list[0][0] == word_list[1][0]
    # ---------------------------------------------------------------------------------------


# Check
print(animal_crackers('Levelheaded Llama'))
# Check
print(animal_crackers('Crazy Kangaroo'))
print(animal_crackers('Learning Centre'))

# 3.


def makes_twenty(n1, n2):
    '''
    MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
    makes_twenty(20,10) --> True
    makes_twenty(12,8) --> True
    makes_twenty(2,3) --> False
    '''
    # Write your code here
    # --------------------------------Code between the lines!--------------------------------
    if n1 == 20 or n2 == 20 or n1 + n2 == 20:
        return True
    else:
        return False
    # ---------------------------------------------------------------------------------------


# Check
print(makes_twenty(20, 10))
# Check
print(makes_twenty(1, 19))
