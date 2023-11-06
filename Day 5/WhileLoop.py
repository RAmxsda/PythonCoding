# multiplication table of 1 to 10 using while loop

i = 1

while i <= 10:
    for j in range(1, 11):
        print(f"{i}*{j} = {i*j}")
    print("\n")
    i = i + 1
