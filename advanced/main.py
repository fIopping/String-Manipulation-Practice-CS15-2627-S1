question = input("1. Format a Name\n"
    "2. Format a Title\n"
    "3. Format a List\n"
    "4. Process Numbers\n"
    "\nEnter your choice: "
)
if question == "1":
    print("Format a Name")

elif question == "2":
    print("Format a Title")

elif question == "3":
    print("Format a List\n")
    answer3 = input("Enter the string to process in the format - apples,oranges,bananas,grapes...\n")

    if "," in answer3:
        answer3 = answer3.replace(","," | ")
        print(answer3.upper())

    if "," not in answer3:
        print("Please enter a valid input")

    else:
        break

    while True:
        guess = input("Guess a hand signal")
        if guess != "Rock" and guess != "Paper" and guess != "Scissors":
            print("Type in Rock, Paper, or Scissors")

        else:
            break