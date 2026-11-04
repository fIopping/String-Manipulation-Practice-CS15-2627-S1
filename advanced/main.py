
def user_choices() -> str:
    choices = ["1", "2", "3", "4"]

    while True:
        print("\nChoose how you would like to process a string:\n")
        print("1. Format a Name")
        print("2. Format a Title")
        print("3. Format a List")
        print("4. Process Numbers")

        choice = input("\nEnter your choice: ")

        if choice in choices:
            return choice
        else:
            print("\nInvalid choice. Please try again.")


def format_name(name: str) -> str:
    name = name.strip().lower()
    last_name, first_name = name.split(",")

    first_name = first_name.strip().title()
    last_name = last_name.strip().title()

    return first_name + " " + last_name


def format_title(title: str) -> str:
    title = title.replace(" ", "")
    title = title.replace(",", " ")
    title = title.replace("::", " ")
    title = title.title()
    title = " ".join(title.split())

    return title


def format_list(items: str) -> str:
    items = items.strip().split(",")

    for i in range(len(items)):
        items[i] = items[i].strip().upper()

    items = " | ".join(items)

    return items


def process_numbers(numbers: str) -> tuple:
    numbers = numbers.strip().split(",")

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i].strip())

    total = sum(numbers)
    average = total / len(numbers)

    return total, average


while True:
    process = user_choices()

    if process == "1":
        name = input("\nEnter your name (Last, First): ")

        try:
            if name.count(",") == 1:
                print(format_name(name))
            else:
                print("Invalid name. Please try again.")

        except (ValueError, IndexError):
            print("Invalid name. Please try again.")

    elif process == "2":
        title = input("\nEnter your title: ")

        if title.strip():
            print(format_title(title))
        else:
            print("Invalid title. Please try again.")

    elif process == "3":
        items = input("\nEnter your list: ")

        if len(items.split(",")) >= 2 and all(item.strip() for item in items.split(",")):
            print(format_list(items))
        else:
            print("Invalid list. Please enter at least 2 items.")

    elif process == "4":
        numbers = input("\nEnter your four numbers: ")

        try:
            number_list = numbers.strip().split(",")

            if len(number_list) == 4:
                total, average = process_numbers(numbers)

                print("Total:", total)
                print("Average:", average)

            else:
                print("Please enter exactly four numbers.")

        except ValueError:
            print("Invalid numbers. Please try again.")
