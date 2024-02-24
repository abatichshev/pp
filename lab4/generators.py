def squares_generator(N):
    for i in range(N):
        yield i ** 2


N = 10
squares = squares_generator(N)
for square in squares:
    print(square)



def even_numbers_generator(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter the value of n: "))
even_numbers = even_numbers_generator(n)
print("Even numbers between 0 and", n, ":", end=" ")
for num in even_numbers:
    print(num, end=", ")


def divisible_by_3_and_4(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


start_range = 0
end_range = 50
numbers_divisible = divisible_by_3_and_4(start_range, end_range)
print("Numbers divisible by 3 and 4 between", start_range, "and", end_range, ":")
for num in numbers_divisible:
    print(num, end=", ")


def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = 3
b = 7
print("Squares of numbers from", a, "to", b, ":")
for square in squares(a, b):
    print(square)


def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = 5
print("Countdown from", n, "to 0:")
for num in countdown(n):
    print(num)
