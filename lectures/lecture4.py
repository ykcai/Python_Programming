# More Function Practice
# Level 1 Problems


def old_macdonald(name):
    '''
    Write a function that captializes the first and fourth letters of name
    If the name is less than 4 letters, return "Name is too short!"
    old_macdonald('macdonald') --> MacDonald
    '''
    if len(name) < 4:
        return "Name is too short!"
    else:
        # [0:3] -> 0 1 2, does not include 3
        return name[0:3].capitalize() + name[3:].capitalize()


print(old_macdonald("macdonald"))
print(old_macdonald("macbook"))


def master_yoda(sentence):
    '''
    Given a sentence, return the words reversed
    '''
    word_list = sentence.split(" ")
    # Cheating
    # word_list.reverse()

    return " ".join(word_list[::-1])


print(master_yoda('I am home'))  # --> 'home am I'
print(master_yoda('We are ready'))  # --> 'ready are We'

# Level 2


def has_33(nums):
    '''
    Given a list of ints, return True if the array contains a 3 next to a 3 somwhere
    '''
    print(nums)
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            # nums[i:i+2] == [3,3]
            return True
    return False


print(has_33([1, 3, 3]))  # → True
print(has_33([1, 3, 1, 3]))  # → False
print(has_33([3, 1, 3]))  # → False

# Challenge Problem


def spy_game(nums):
    '''
    Write a function that take in a list of integers and returns
    True if it contains 007 in ORDER
    '''
    print(nums)
    # for i in range(0, len(nums) - 1):
    # if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
    #     return True
    # return False
    code = [0, 0, 7, 'x']
    for a in nums:
        if a == code[0]:
            code.pop(0)  # remove the first element in code
            print(code)
    return code == ['x']


print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # --> True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # --> True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # --> False
print(spy_game([1, 3, 4, 5, 3, 2, 3, 544, 0, 2, 3, 34, 5, 0, 3,
                2, 3, 45, 5, 6, 4, 3, 2, 7, 1, 23, 4, 5, 4, 3, 2]))  # --> True

# Fun Question


def print_big(letter):
    patterns = {
        1: '  *  ',
        2: ' * * ',
        3: '*   *',
        4: '*****',
        5: '**** ',
        6: '   * ',
        7: ' *   ',
        8: '*  * ',
        9: '*    ',
        10: '* ***'
    }
    alphabet = {
        'A': [1, 2, 4, 3, 3],
        'B': [5, 3, 5, 3, 5],
        'C': [4, 9, 9, 9, 4],
        'D': [5, 3, 3, 3, 5],
        'E': [4, 9, 4, 9, 4],
        'F': [4, 9, 4, 9, 9],
        'G': [4, 9, 10, 3, 4]
    }

    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


print_big('a')
print_big('b')
print_big('c')
print_big('d')
