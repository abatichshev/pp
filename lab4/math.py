import math

degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print("Output radian:", radian)


    height = float(input("Height: "))
base1 = float(input("first value: "))
base2 = float(input("second value: "))
area = 0.5 * (base1 + base2) * height
print("Expected Output:", area)




import math

num_sides = int(input())
side_length = float(input())
area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
print("The area of the polygon is:", area)


base = float(input(""))
height = float(input(""))
area = base * height
print("Expected Output:", area)
