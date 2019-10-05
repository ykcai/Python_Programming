
# Week 3 Homework Answers
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

print(7**4)

# ** Split this string:**
#
#     s = "Hi there Sam!"
#
# **into a list. **


s = 'Hi there Sam!'
print(s.split())


# ** Given the variables:**
#
#     planet = "Earth"
#     diameter = 12742
#
# ** Use .format() to print the following string: **
#
#     The diameter of Earth is 12742 kilometers.


planet = "Earth"
diameter = 12742


print("The diameter of {} is {} kilometers.".format(planet, diameter))
print(f"The diameter of {planet} is {diameter} kilometers")
print("The diameter of %s is %s kilometers" %(planet, diameter))


# ** Given this nested list, use indexing to grab the word "hello" **


lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print(lst[3][1][2][0])

# ** Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky **


d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])


# ** What is the main difference between a tuple and a list? **
# Tuple is immutable


# ** Create a function that grabs the email website domain from a string in the form: **
#
#     user@domain.com
#
# **So for example, passing "user@domain.com" would return: domain.com**

def domainGet(email):
    return email.split("@")[1]

# def domainGet(email):
#     return email.split('@')[-1]


print(domainGet('user@domain.com'))
print(domainGet('aweljfawfhu3fh98a@gmail.com'))


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

def findDog(sentence):
    word_list = sentence.lower().split()
    for word in word_list:
        if word == "dog":
            return True
    else:
        return False 

# def findDog(st):
#     return 'dog' in st.lower().split()

print(findDog('Is there a dog here?'))
print(findDog('a;ijlfew;oijh;ijewafi;u?'))

# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

def countDog(sentence):
    count = 0
    for word in sentence.lower().split():
        if word == "dog":
            count = count + 1
    return count
# def countDog(st):
#     count = 0
#     for word in st.lower().split():
#         if word == 'dog':
#             count += 1
#     return count
print(countDog('This dog runs faster than the other dog dude!'))


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
#
#     seq = ['soup','dog','salad','cat','great']
#
# **should be filtered down to:**
#
#     ['soup','salad']


seq = ['soup', 'dog', 'salad', 'cat', 'great']

def startWithS(input_list):
    answer = []
    for word in input_list:
        if word.lower()[0] == 's':
            answer.append(word)
    return answer

print(startWithS(seq))
# print(list(filter(lambda word: word[0] == 's', seq)))


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all
#   cases. **


def caught_speeding(speed, is_birthday):
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed

    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'

print(caught_speeding(81, True))
print(caught_speeding(81, False))
print(caught_speeding(86, True))
print(caught_speeding(65, True))



# # Great job!
