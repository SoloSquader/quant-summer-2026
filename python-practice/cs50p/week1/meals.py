def main():
    answer = input("What's the time? ")
    answer = convert(answer)
    if (7<=answer<=8):
        print("Breakfast time.")
    elif (12<=answer<=13):
        print("Lunch time.")
    elif (18<=answer<=19):
        print("Dinner time.")

def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes)
    hours = int(hours)
    return hours + minutes / 60


main()