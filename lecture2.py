# while Loops
i = 1
while i<5:
    print("i is: {}".format(i))
    i = i+1

# range()
print(range(5))

for number in range(5):
    print(number)


# list comprehension

x = [1, 2, 3, 4]
output=[]
for item in x:
    output.append(item**2)

print(output)

print([item**2 for item in x])

# functions
def my_func(param1="nothing1", param2="nothing2", param3="nothing3"):
    print(param1, param2, param3)

my_func("hello", "class", 123456789)
my_func()

def square(x):
    return x**2

print(square(5))

# lambda

def times2(var):
    return var*2

print(times2(42))

lambda var: var*2

answer = lambda var: var*2

print(answer(2))

