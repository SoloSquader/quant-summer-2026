remainder = 50

while (remainder > 0):
    answer = input("How much would you like to put in? ")
    answer = int(answer)
    if (answer != 25 and answer != 5 and answer != 10):
        print(f"Amount due: {remainder}")
        remainder = remainder
    elif (remainder-answer <= 0):
        neg = abs(remainder-answer)
        
        print(f"Change Owed: {neg}")
        break

    else:
        remainder = remainder - answer
        print(f"Amount due: {remainder}")