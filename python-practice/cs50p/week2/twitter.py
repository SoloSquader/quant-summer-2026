answer = input("")


for letter in answer:
    temp = letter
    letter = letter.lower()
    if (letter != "a" and letter != "e" and letter != "i" and letter != "o" and letter != "u"):
        print(temp, end = "")
    
