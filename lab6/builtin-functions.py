from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = input().split
result = multiply_list(numbers)
print("Result:", result)




def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

string = "Hello World"
upper, lower = count_upper_lower(string)
print("Upper case count:", upper)
print("Lower case count:", lower)


def is_palindrome(string):
    return string == string[::-1]

string = "radar"
if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a palindrome")



import time
import math

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

number = 25100
milliseconds = 2123
result = square_root_after_milliseconds(number, milliseconds)
print("Square root of", number, "after", milliseconds, "milliseconds is", result)



def all_true(tuple_values):
    return all(tuple_values)

tuple_values = (True, True, False, True)
print(all_true(tuple_values))



