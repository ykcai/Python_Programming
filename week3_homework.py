# Week 3 Homework
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

''' ** What is 7 to the power of 4?'''
# --------------------------------Code between the lines!--------------------------------


# ---------------------------------------------------------------------------------------

'''Split this following string into a list.'''
# --------------------------------Code between the lines!--------------------------------
s = "Hi there Sam!"

# ---------------------------------------------------------------------------------------

'''** Given the variables:**

    planet = "Earth"
    diameter = 12742

** Use string formatting to print the following string: **
    Google this if you don't know!

Output: The diameter of Earth is 12742 kilometers.'''
# --------------------------------Code between the lines!--------------------------------

planet = "Earth"
diameter = 12742
# ---------------------------------------------------------------------------------------



# ** Given this nested list, use indexing to grab the word "hello" **

# --------------------------------Code between the lines!--------------------------------
lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]

# ---------------------------------------------------------------------------------------

# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **
# --------------------------------Code between the lines!--------------------------------
d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man',
                                 'inception', {'target': [1, 2, 3, 'hello']}]}]}

# ---------------------------------------------------------------------------------------

# ** Create a function that grabs the email website domain from a string in the form: **
#
#     user@domain.com
#
# **So for example, passing "user@domain.com" would return: domain.com**
# --------------------------------Code between the lines!--------------------------------


domainGet('user@domain.com')
# ---------------------------------------------------------------------------------------



# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **
# --------------------------------Code between the lines!--------------------------------

findDog('Is there a dog here?')

# ---------------------------------------------------------------------------------------


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **
# --------------------------------Code between the lines!--------------------------------


countDog('This dog runs faster than the other dog dude!')
# ---------------------------------------------------------------------------------------



# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
#
#     seq = ['soup','dog','salad','cat','great']
#
# **should be filtered down to:**
#
#     ['soup','salad']
# --------------------------------Code between the lines!--------------------------------


seq = ['soup', 'dog', 'salad', 'cat', 'great']
# ---------------------------------------------------------------------------------------



# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all
#   cases. **
# --------------------------------Code between the lines!--------------------------------
def caught_speeding(speed, is_birthday):
    pass


caught_speeding(81, True)


caught_speeding(81, False)
# ---------------------------------------------------------------------------------------

# # Great job!
