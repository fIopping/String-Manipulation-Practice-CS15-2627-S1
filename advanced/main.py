
def user_choices() -> str:
    choices = ["1", "2", "3", "4"]

    while True:
        print("Choose a process:\n")
        print("1. Format a Name")
        print("2. Format a Title")
        print("3. Format a List")
        print("4. Process Numbers")

        choice = input("\nEnter your choice: ")

        if choice in choices:
            return choice
        else:
            print("\nPlease enter a number from the list.\n")


def format_name(name: str) -> str:
    name = name.strip().lower().split(",")
    first_name = name[1].strip().title()
    last_name = name[0].strip().title()
    return first_name + " " + last_name


def format_title(title: str) -> str:
    title = title.replace(",", " ").replace(":", " ")
    title = title.lower().title()
    title = " ".join(title.split())
    return title


def format_list(items: str) -> str:
    items = items.upper().strip().split(",")
    items = " | ".join(items)
    return items


def process_numbers(numbers: str) -> tuple:
    numbers = numbers.strip().split(",")

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    total = sum(numbers)
    average = total / len(numbers)

    return total, average


while True:
    process = user_choices()

    if process == "1":
        name = input("\nEnter your name (Last, First): ")

        if name.count(",") == 1:
            print(format_name(name))
        else:
            print("Invalid name. Please try again.")

    elif process == "2":
        title = input("\nEnter your title: ")

        if title.strip():
            print(format_title(title))
        else:
            print("Invalid title. Please try again.")

    elif process == "3":
        items = input("\nEnter your list: ")

        if len(items.split(",")) >= 2:
            print(format_list(items))
        else:
            print("Invalid list. Please try again.")

    elif process == "4":
        numbers = input("\nEnter your four numbers: ")

        try:
            numbers_list = numbers.strip().split(",")

            if len(numbers_list) == 4:
                for number in numbers_list:
                    int(number.strip())

                total, average = process_numbers(numbers)
                print("Total:", total)
                print("Average:", average)
            else:
                print("Please enter exactly four numbers.")

        except ValueError:
            print("Please enter valid numbers.")
