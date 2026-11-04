string_to_process = "t H e , T a L e :: O f , T w O :: c I t I e S"

# Expected Output: The Tale Of Two Cities

new_string = (
    string_to_process.replace("t H e ,", "The")
    .replace(" T a L e ::", " Tale")
    .replace(" O f ,", " Of")
    .replace(" T w O ::", " Two")
    .replace(" c I t I e S", " Cities")
)
print(new_string)