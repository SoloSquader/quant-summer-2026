# asks for name, removes white space, capitalizes every word
name = input("Type your name: ").strip().title()

first, last = name.split(" ")


print(f"Hello, {first}!")
