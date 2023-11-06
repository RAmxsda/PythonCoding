import math

height = input("Enter your height in m:")
weight = input("Enter your weight in kg:")

bmi = int(weight) / float(height) ** 2

print(bmi);
print(round(bmi));

# math.ceil() rounds up to the nearest integer
print(math.ceil(bmi))

# math.floor() rounds down to the nearest integer
