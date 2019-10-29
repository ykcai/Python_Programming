# Python Programming Week 6 Homework

# 1. Write a Python function to find the Max of three numbers. Hint, make the max_of_two function first!


def max_of_two(x, y):
    if x > y:
        return x
    return y


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))


print(max_of_three(3, 6, -5))

# 2. Write a Python function to sum all the numbers in a list.
# Sample List: (8, 2, 3, 0, 7)
# Expected Output: 20


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total


print(sum((8, 2, 3, 0, 7)))


# 3. Write a Python function to multiply all the numbers in a list.
# Sample List: (8, 2, 3, -1, 7)
# Expected Output: -336
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


print(multiply((8, 2, 3, -1, 7)))

# 4. Write a Python program to reverse a string.
# Sample String: "1234abcd"
# Expected Output: "dcba4321"


def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index = index - 1
    return rstr1


print(string_reverse('1234abcd'))

# 5. Write a Python function to calculate the factorial of a number(a non-negative integer). The function accepts the number as an argument.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


n = int(input("Input a number to compute the factiorial : "))
print(factorial(n))


# 6. Write a Python function to check whether a number is in a given range.
def test_range(n):
    if n in range(3, 9):
        print(" %s is in the range" % str(n))
    else:
        print("The number is outside the given range.")


test_range(5)


# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String: 'The quick Brow Fox'
# Expected Output:
# No. of Upper case characters: 3
# No. of Lower case Characters: 12
def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["UPPER_CASE"])
    print("No. of Lower case Characters : ", d["LOWER_CASE"])


string_test('The quick Brown Fox')


# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List: [1, 2, 3, 3, 3, 3, 4, 5]
# Unique List: [1, 2, 3, 4, 5]
def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))


# 9. Write a Python function that takes a number as a parameter and check the number is prime or not.
# Note: A prime number(or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
def test_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if(n % x == 0):
                return False
        return True


print(test_prime(9))


# 10. Write a Python program to print the even numbers from a given list.
# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result: [2, 4, 6, 8]
def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum


print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 11. Write a Python function to check whether a number is perfect or not.
# According to Wikipedia: In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself(also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors(including itself).
# Example: The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: (1 + 2 + 3 + 6) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


print(perfect_number(6))


# 12. Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True


print(isPalindrome('aza'))
