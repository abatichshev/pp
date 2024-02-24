#A recipe you are reading states how many grams you need for the ingredient. 
# Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces.
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = float(input())
ounces = grams_to_ounces(grams)
print(f"{ounces:.2f}")

# Read in a Fahrenheit temperature.
#  Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)



fahrenheit = float(input())
celsius = (5 / 9) * (fahrenheit - 32)
print(f"{celsius:.2f} ")

# Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have? 

def is_prime(n):
   
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):

    return [num for num in numbers if is_prime(num)]


numbers_input = input()
numbers_list = list(map(int, numbers_input.split()))

prime_numbers = filter_prime(numbers_list)
print(prime_numbers)

def reverse_sentence(sent):
    words = sent.split()  
    reversed_words = reversed(words) 
    reversed_sentence = ' '.join(reversed_words) 
    return reversed_sentence


x = input()
reversed_sentence = reverse_sentence(x)
print(reversed_sentence)
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]) )
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
def spy_game(nums):
  
    found_zero = False
    found_double_zero = False
    
  
    for num in nums:
        if num == 0:
            if found_zero:
                found_double_zero = True
            else:
                found_zero = True
        elif num == 7 and found_double_zero:
            return True
    
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))   
print(spy_game([1, 0, 2, 4, 0, 5, 7]))   
print(spy_game([1, 7, 2, 0, 4, 5, 0]))   


def sph_volume(radius):
    
    volume = (4/3) * 3.14 * radius ** 3
    
    return volume

radius = int(input())

volume = sph_volume(radius)

print(volume)


def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


print(unique_elements([1, 2, 2, 3, 4, 4, 5]))  

def is_palindrome(word):
   
    word = word.replace(" ", "").lower()
    return word == word[::-1]


print(is_palindrome("madam"))  
print(is_palindrome("hello"))  

def histogram(nums):
    for num in nums:
        print("*" * num)


histogram([4, 9, 7])

import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    number_to_guess = random.randint(1, 20)
    guesses_taken = 0

    while True:
        guess = int(input("Take a guess.\n"))
        guesses_taken += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break


guess_the_number()

