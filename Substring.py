#A zero corresponds to players of one team; a one corresponds to players of another team. If there are at least 7 players of some team standing one after another, then the situation is considered dangerous
string = input()
if "1111111" in string or "0000000" in string:
    print("Dangerious")
else:
    print("Not Dangerious")