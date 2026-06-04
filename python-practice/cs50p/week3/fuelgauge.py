while True:
    try:
        x = input("What is your fraction? ")
        numerator, denominator = x.split("/")
        numerator = int(numerator)
        denominator = int(denominator)
        if denominator == 0 or numerator>denominator or numerator<0 or denominator<0:
            continue

    except(ValueError, ZeroDivisionError):
        pass

    else:
        
        rounded = round(float((numerator/denominator))*100)
        if (rounded<=1):
            print("E")
            break
        elif (rounded>=99):
            print("F")
            break
        else:
            print(f"{rounded}%")
            break