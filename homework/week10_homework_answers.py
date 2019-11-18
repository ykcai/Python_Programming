
# Python Programming Week 10 Homework Answers

# 1. Create a function that counts the number of adverbs in a sentence. An adverb is a word that ends with ly.

# count_adverbs("She ran hurriedly towards the stadium.") ➞ 1
# count_adverbs("She ate the lasagna heartily and noisily.") ➞ 2
# count_adverbs("He hates potatoes.") ➞ 0
# count_adverbs("He was happily, crazily, foolishly over the moon.") ➞ 3

# Notes: Do NOT count words where the ly is in the beginning or the middle (e.g. Lysol, Illya). For the purpose of this exercise, ignore the nuances of the English language (some adjectives also end in ly).


def count_adverbs(sentence):
    lst = sentence.split()
    count = 0
    for word in lst:
        if "ly" in word:
            count += 1
    return count


print(count_adverbs("She ran hurriedly towards the stadium."))
print(count_adverbs("She ate the lasagna heartily and noisily."))
print(count_adverbs("He hates potatoes."))
print(count_adverbs("He was happily, crazily, foolishly over the moon."))


# 2. Create a function that takes an array of 10 numbers (between 0 and 9) and returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555).

# formatPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) ➞ "(123) 456-7890"
# formatPhoneNumber([5, 1, 9, 5, 5, 5, 4, 4, 6, 8]) ➞ "(519) 555-4468"
# formatPhoneNumber([3, 4, 5, 5, 0, 1, 2, 5, 2, 7]) ➞ "(345) 501-2527"
# Notes: Don't forget the space after the closing parenthese.

def format_phone_numer(phone_number):
    return (f"({phone_number[0]}{phone_number[1]}{phone_number[2]}) {phone_number[3]}{phone_number[4]}{phone_number[5]}-{phone_number[6]}{phone_number[7]}{phone_number[8]}{phone_number[9]}")


print(format_phone_numer([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(format_phone_numer([5, 1, 9, 5, 5, 5, 4, 4, 6, 8]))
print(format_phone_numer([3, 4, 5, 5, 0, 1, 2, 5, 2, 7]))

# 3. Create a function which takes in a word and spells it out, by consecutively adding letters until the full word is completed.

# spelling("bee") ➞ ["b", "be", "bee"]
# spelling("happy") ➞ ["h", "ha", "hap", "happ", "happy"]
# spelling("eagerly") ➞ ["e", "ea", "eag", "eage", "eager", "eagerl", "eagerly"]


def spelling(word):
    ans = []
    for x in range(1, len(word)+1):
        ans.append(word[:x])
    return ans


print(spelling("bee"))
print(spelling("happy"))
print(spelling("eagerly"))
