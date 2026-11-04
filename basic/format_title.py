string_to_process = "t H e , T a L e :: O f , T w O :: c I t I e S"


title = string_to_process.replace(" ", "")
title = title.replace(",", " ")
title = title.replace("::", " ")
title = title.title()
title = " ".join(title.split())
print(title)
# Expected Output: The Tale Of Two Cities