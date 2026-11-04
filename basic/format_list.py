from unittest import result

string_to_process = "eggs,cheese,milk,bread,cereal"

# Expected Output: "EGGS | CHEESE | MILK | BREAD | CEREAL"

split_list = string_to_process.split(",")

result = " | ".join(split_list).upper()

print(result)