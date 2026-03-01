# todo.py

FILE_NAME = "to_do.txt"

while True:
    choice = input('Do you want to add a new To-Do item? (y/n) or type "exit": ').strip().lower()

    if choice == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break

    if choice == "y":
        item = input("Type your new To-Do item: ").strip()
        if item:  # لا يحفظ سطر فاضي
            with open(FILE_NAME, "a", encoding="utf-8") as f:
                f.write(item + "\n")
        continue

    if choice == "n":
        read_choice = input("Do you want to list your To-Do items? (y/n): ").strip().lower()
        if read_choice == "y":
            try:
                with open(FILE_NAME, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:
                        print(content)  # يطبع كل سطر (كل مهمة) في سطر
                    else:
                        print("Your To-Do list is empty.")
            except FileNotFoundError:
                print("No To-Do file found yet. Add items first.")
        continue

    print("Invalid choice. Please type y, n, or exit.")