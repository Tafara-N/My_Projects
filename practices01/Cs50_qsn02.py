expression = input("Expression: ")

x, y, z = expression.split(" ")
x = float(x)
z = float(z)

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

print(f"{result:.1f}")
