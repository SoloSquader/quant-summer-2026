answer = input("What is your variable name, in camelCase? ")

for letter in answer:
    if (letter==answer[0] and letter.isupper()):
        print(letter[0].lower(), end = "")
    elif (letter.isupper()):
        print(f"_{letter.lower()}", end = "")
    else:
        print(letter, end = "")

