string_to_process = "   sMitH, aLeX    "
string_to_process = string_to_process.replace(", ", " ".replace("sMith", "Alex").replace("aLeX", "Smith"))

print(str(string_to_process).strip().title())
# Expected output: "Alex Smith"