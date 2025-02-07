# lets create a journal
with open("journal.txt", "a") as journal:
    while True: # Infinite loop until loop is pressed
        text = input("enter a journal entry: (press q to quit): ")
        if text == "q":
            break
        journal.write(text.capitalize()+"\n")