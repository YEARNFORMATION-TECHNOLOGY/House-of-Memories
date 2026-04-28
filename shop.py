with open("Shopping List.py", "r") as f:
    shopping_list = f.read()

with open("Shopping List.txt", "w") as f:
    f.write(shopping_list)