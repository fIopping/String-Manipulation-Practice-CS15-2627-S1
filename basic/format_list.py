string_to_process = "eggs,cheese,milk,bread,cereal"
string_to_process = string_to_process.replace(",", " | ")
print(str(string_to_process).upper())

# Expected Output: "EGGS | CHEESE | MILK | BREAD | CEREAL"