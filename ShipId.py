#program that takes in a letterclass ID of a ship and display the equivalent string class description of the given ID. Use the table below.
for i in range(int(input())):
    id = input()
    if id == 'B' or id == 'b':
        print("battle Ship")
    elif id == 'C' or id == 'c':
        print("Cruiser")
    elif id == 'D' or id == 'd':
        print("Destroyer")
    elif id == 'F' or id == 'f':
        print("Frigate")
    else:
        print("Enter valid ID")