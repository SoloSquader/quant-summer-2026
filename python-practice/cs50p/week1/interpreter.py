answer = input("")

x, y, z = answer.split(" ")

x = float(int(x))
z = float(int(z))

if (y == "+"):
    result = x+z
elif (y == "-"):
    result = x-z
elif (y == "/"):
    result = x/z
elif (y == "*"):
    result = x*z

print(f"{result:.1f}")

