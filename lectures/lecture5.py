# Lambda Expressions, Map and Filter

# Definition
# Map Function: allows you to "map" a function to an iterable object. That is to same you can quickly call the same function to every item in an iterable, such as a list.


def square(num):
    return num ** 2


my_list = [2, 4, 6, 8, 10]
result = map(square, my_list)
print(list(result))


def splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'even'
    else:
        return my_string[0]


my_names = ['Edwin', "Sean", "Shawn", "Michael", "Crystal"]
result = list(map(splicer, my_names))
print(result)

# Definition
# Filter Function: returns an iterator yielding those items of iterable for which function(item) is true. Passing an iterable into a filter will get back only the results that would return True in the function.


def greater_than_3(num):
    if num > 3:
        return True
    else:
        return False


def check_even(num):
    return num % 2 == 0


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(check_even, nums))
print(result)
result = list(filter(greater_than_3, nums))
print(result)

# Definition
# Lambda Expression: allows us to create "anonymous" functions. Basically, we can make ad-hoc functions without needing to define a function using DEF


# def square2(num):
#     result = num**2
#     return result

# def square2(num):
#     return num**2

# def square2(num): return num**2

# square2 = lambda num: num**2

# print(square2(2))

print(my_list)
result = list(map(lambda num: num**2, my_list))
print(result)

result = list(filter(lambda n: n % 2 == 0, nums))
print(result)

result = map(lambda x: x+x, filter(lambda x: x > 3, nums))
print(list(result))
# filter -> [4, 5, 6, 7, 8, 9, 10]
# map -> [8, 10, 12, 14, 16, 18, 20]

# Nested Statements and Scope
# Definition
# Scope: Variable names have a scope, the scope determines the visibility of that varbiale name to other parts of your code. This also applies to functions!!!!!
x = 25


def printer():
    x = 50
    return x


print(x)
print(printer())

# LEGB Rule:
'''
Local: Names assigned in any way within a function (def or lambda)
Enclosing Function Locals: Names in the local scope of any and all enclosing functions, from inner to outer
Global (module): Names assigned at the top-level of a module file, or delcared global in a def within the file
Built-in (Python): Names preassigned in built-in names (range, map, filter, etc..)
'''

# Local
# def f(x): return x+2
# f = lambda x: x+2
# x is a local scoped variable

# Enclosing function locals
name = "This is a global name"


def greet():
    # Enclosing function
    name = "Michael"

    def hello():
        print('Hello ' + name)

    hello()


greet()

# Global
print(name)

# Built-in
# filter
# len
# print
# map
# while
# for
# and
# in
# or
