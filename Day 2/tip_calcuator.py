bill = int(input("Enter the bill amount: "));
percentage = int(input("Enter the percentage of tip you would provide:"));
people = int(input("Enter the number of people: "));
payement = (bill + (bill * percentage / 100)) /people;

print(f"The total amount is: {bill + (bill * percentage / 100)} \nEach person should pay: {payement:.2f} ")