# Python Programming Week 7 Homework Answers

# 1. Write a shutting down program:
# First, def a function, shut_down, that takes one argument s. Then, if the shut_down function receives an s equal to "yes", it should return "Shutting down" Alternatively, elif s is equal to "no", then the function should return "Shutdown aborted". Finally, if shut_down gets anything other than those inputs, the function should return "Sorry".
   def shut_down(s):
        if s == "yes":
            return "Shutting down"
        elif s == "no":
            return "Shutdown aborted"
        else:
            return "Sorry"

s = "no"
shut_down(s)

# 2. Import the math module in whatever way you prefer. Call its sqrt function on the number 13689 and print that value to the console.

from math import sqrt
print(sqrt(13689))

# 3. First, def a function called distance_from_zero, with one argument (choose any argument name you like). If the type of the argument is either int or float, the function should return the absolute value of the function input. Otherwise, the function should return "Nope". Check if it works calling the function with -5.6 and "what?".

   def distance_from_zero(num):
        if type(num) == int or type(num) == float:
            return abs(num)
        else:
            return "Nope"

distance_from_zero(-5.6)
5.6
distance_from_zero("what?")
# 4. Rewrite the pay computation program with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0


def computepay(hours, rate):
    hours = float(hours)
    rate = 10
    if hours < 40:
        pay = hours*rate
        print("the pay is:", pay)
    else:
        pay = 40 * rate + (hours-40)*1.5*rate
        print("the pay is:", pay)
    return pay


print(475.0, computepay(45, 10))
