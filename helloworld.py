# single word
print("Bananas")

# phrase
print("Hello World, my name is Michael!")
# single quotes
print('I\'ll be using single quotes')

# create a set

x = set()
x.add("hello")
x.add('bye')
x.add('bye')
x.add('bye')
x.add('bye')
x.add('bye')
x.add('bye')
x.add('bye')
x.add('bye')
x.add('bye')
x.add("bye")
print(x)

print(100.25 * 1 + 1 - 1 / 1 ** 1)
print((60 + (10**2) / 4 * 7) - 134.75)

x = 3 + 1.5 + 4
print(type(x))

s = 'hello'
answer = 'olleh'
print(s[4],s[3],s[2],s[1],s[0])
print(s[::-1])
print(s[::])
print(s[-1], s[4])

[0,0,0]

s = [0,0,0]
a = [0]*3
print(s, a)

# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
['Print', 'only', '..']
for word in st.split():
    if word[0] == "s":
        print(word)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string' 
answer = ['C', 'a', 'l', 'o', 't']
answer = []
# print(st.split())

for word in st.split():
    print(word)

# answer = [word[0] for word in st.split()]
# print(answer)


