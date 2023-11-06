# import random

# name = input("Enter names seprated by comma ")
# name_split = name.split(',')
# print("\n",name_split)

# length_names = len(name_split)
# print("\n",length_names);

# selected_name=random.randint(0,length_names-1)
# print(f"\n{name_split[selected_name]} has to pay the whole bill");


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map=[row1,row2,row3]

print(map);
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

if (len(position) != 2 ):
    print("Invalid input")
    exit()

# as an instant when we enter "23"
horizontal = int(position[0]) # Entered 2 is horizontal

vertical = int(position[1]) # Entered 3 is vertical

map[vertical-1][horizontal-1] = "X" # to change the value of the list with "X";

print(f"{row1}\n{row2}\n{row3}")