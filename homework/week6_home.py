# Python Programming Week 6 Homework

# 1. Write a Python function to find the Max of three numbers. Hint, make the max_of_two function first!


def max_of_two(x, y):
    pass


def max_of_three(x, y, z):
    pass


print(max_of_three(3, 6, -5))

# 2. Write a Python function to sum all the numbers in a list.
# Sample List: (8, 2, 3, 0, 7)
# Expected Output: 20


def sum(numbers):
    pass


print(sum((8, 2, 3, 0, 7)))


# 3. Write a Python function to multiply all the numbers in a list.
# Sample List: (8, 2, 3, -1, 7)
# Expected Output: -336
def multiply(numbers):
    pass


print(multiply((8, 2, 3, -1, 7)))

# 4. Write a Python program to reverse a string.
# Sample String: "1234abcd"
# Expected Output: "dcba4321"


def string_reverse(str1):
    pass


print(string_reverse('1234abcd'))

# 5. Write a Python function to calculate the factorial of a number(a non-negative integer). The function accepts the number as an argument.


def factorial(n):
    pass


n = int(input("Input a number to compute the factiorial : "))
print(factorial(n))


# 6. Write a Python function to check whether a number is in a given range.
def test_range(n):
    pass


test_range(5)


# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
# I have started this questions and the FOR loop, just fill in the code in the loop to make it work!


def up_low(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List: [1, 2, 3, 3, 3, 3, 4, 5]
# Unique List: [1, 2, 3, 4, 5]
def unique_list(l):
    pass


print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))


# 9. Write a Python function that takes a number as a parameter and check the number is prime or not.
# Note: A prime number(or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
def test_prime(n):
    pass


print(test_prime(9))


# 10. Write a Python program to print the even numbers from a given list.
# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result: [2, 4, 6, 8]
def is_even_num(l):
    pass


print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 11. Write a Python function to check whether a number is perfect or not.
# According to Wikipedia: In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself(also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors(including itself).
# Example: The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: (1 + 2 + 3 + 6) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
def perfect_number(n):
    pass


print(perfect_number(6))


# 12. Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def isPalindrome(string):
    pass


print(isPalindrome('aza'))
