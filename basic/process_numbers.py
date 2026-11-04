string_to_process = "  18,27,35,20  "

numbers = string_to_process.strip()
numbers = numbers.split(",")
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
total = sum(numbers)
average = total / len(numbers)
print("total:", total)
print("average:", average)
