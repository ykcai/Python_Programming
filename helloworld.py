# single word
print("Bananas")

# phrase
print("Hello World, my name is Michael!")
# single quotes
print("I'll be using single quotes")

# create a set

x = set()
x.add("hello")
x.add("bye")
x.add("bye")
x.add("bye")
x.add("bye")
x.add("bye")
x.add("bye")
x.add("bye")
x.add("bye")
x.add("bye")
x.add("bye")
print(x)

print(100.25 * 1 + 1 - 1 / 1 ** 1)
print((60 + (10 ** 2) / 4 * 7) - 134.75)

x = 3 + 1.5 + 4
print(type(x))

s = "hello"
answer = "olleh"
print(s[4], s[3], s[2], s[1], s[0])
print(s[::-1])
print(s[::])
print(s[-1], s[4])

[0, 0, 0]

s = [0, 0, 0]
a = [0] * 3
print(s, a)

# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = "Print only the words that start with s in this sentence"
["Print", "only", ".."]
for word in st.split():
    if word[0] == "s":
        print(word)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = "Create a list of the first letters of every word in this string"
answer = ["C", "a", "l", "o", "t"]
answer = []
# print(st.split())

for word in st.split():
    print(word)

# answer = [word[0] for word in st.split()]
# print(answer)

# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

word = "hello"
["h", "e", "l", "l", "o"]
answer = "e"
# word[1] = "a"

# Reassign 'hello' in this nested list to say 'goodbye' instead:

list3 =[1,2,[3,4,'hello']]
list3[2][2] = "goodbye"
print(list3)
a = False
b = True
if a :
    print("we got here!")
elif b:
    print("b was true")
else:
    print("we got to the else")

print("exited if block")

numList = [1,2,3,4,5,6]

for num in numList:
    if num % 2 == 0:
        print("This number remainder of 0: ", num)
    else: 
        print("This number does not have remainder of 0: ", num)

list_sum = 0

for num in numList:
    list_sum = list_sum + num

print(list_sum)

for letter in "This is my long, very long, string of text":
    print(letter)

tup = (1,2,3,4,5)

for value in tup:
    print(value)

new_list = [1,2,3,4, [1,2,3], "nested", ["new", "list"]]

for item in new_list:
    if isinstance(item, str) :
        print(type(item))
        print(item)

d = {"k1": 4, "k2": 2, "k3": 3}
for key, value in d:
    print(key, " : ", value)

d.keys()
d.values()

# To create a list of all numbers between 1 and 10 that are divisible by 3
input_list = [1,2,3,4,5,6,7,8,9,10]
answer = []
# # add element to list
# answer.append(3)
# answer = [3, 6, 9]
# print(answer)

for number in input_list:
    if number % 3 == 0:
        print(number)
        answer.append(number)

print(number)

# While Loops



