try:
    with open("example.txt", "x") as f:
        f.write("Hello, World!")
except FileExistsError:
    pass
    
Items = []
try:
    with open("Shopping List.txt", "r") as f:
        
        Items = [line.strip() for line in f.readlines() if line.strip()]
except FileNotFoundError:
    print("No previous shopping list found. Starting fresh.")

while True:
    try:
        print("\nShopping List Manager")
        print("1. Add an Item")
        print("2. Remove Item")
        print("3. View Items")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter item name: ")
            Items.append(name)
            print("Item added!")

        elif choice == "2":
            name = input("Enter item to remove: ")
            if name in Items:
                Items.remove(name)
                print("Item removed!")
            else:
                print("Item not found.")

        elif choice == "3":
            print("\nShopping List:")
            if not Items:
                print("No items yet.")
            else:
                for item in Items:
                    print("-", item)

        elif choice == "4":
            with open("Shopping List.txt", "w") as f:
                for item in Items:
                    f.write(item + "\n")
            print("List saved. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
        break
    except Exception as e:
        print("An error occurred:", e)
