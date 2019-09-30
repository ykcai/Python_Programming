# Methods
# defintion: methods perform specific actions on an object and can also take arguments

# Create a simple list
my_list = [1,2,3,4,5]

# append, count, extend, insert, pop, remove, reverse, sort

my_list.append("whatever")
my_list.append([12])
my_list.append((1,2,4,4,5,5)) # this is appending a tuple
print(my_list)
my_list.reverse()
print(my_list)
my_list.append([5, 4, 3, 2, 1])
print(my_list)
print(my_list.count(5))

# Functions
# definition: a function is a useful device that groups together a set of statements so they can be run more than once

# def count(arg1):
#     ...

def name_of_function(arg1, arg2):
    '''
    This is where the function's Document String (docstring) goes
    This place tells the developer what this function does
    '''
    # Do stuff here
    # Return desired result

def say_hello():
    print("h e l l o")

say_hello()

def greeting(name):
    print("Hello %s" %(name))
    print(f"Hello {name}")

greeting("Michael")

def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

print(add_numbers(4.8761, 12.249))
print(add_numbers("one", "two"))

def is_prime(num):
    '''
    Naive method of checking for primes.
    '''
    for n in range(2, num):
        if num % n == 0:
            print(f"{num} is not a prime!")
            break
    else: # If never equal to 0, then prime
        print(f"{num} is prime!")

is_prime(3)

import math

def is_prime2(num):
    '''
    Better method of checking primes.
    '''
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

print(is_prime2(16))