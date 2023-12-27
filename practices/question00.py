# Question: Write the string after the first occurrence of ',' and the string after the last occurrence of ',' in the string "Hello, Good, Morning". World".

str = "Hello, Good, Morning\". World\"."
print(str[str.find(","): str.rfind(",")])
