n =0
printed = ""
while True:
    try:
        text = input("Name: ")
        
        n=n+1
        if n == 1:
            printed = text
            store1 = text
        elif n == 2:
            printed = printed + " and " + text
            store2 = text
        elif n == 3:
            printed = store1 + ", " + store2 + ", and " + text
        else:
            printed = printed.replace(", and ", ", ")
            printed = printed + ", and " + text

    except EOFError:
        print(f"Adieu, adieu, to {printed}")
        break
