

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        answer = input("Date? ").strip().lower().title()
        if "/" in answer:
            month, day, year = answer.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if(month>12 or day>31 or month<1 or day<1):
                continue
            print(f"{year}-{month:02}-{day:02}")
            break
        else:
            month, day, year = answer.split(" ")
            month = months.index(month) + 1
            day = day.replace(",", "")
            day = int(day)
            year = int(year)
            if(month>12 or day>31 or month<1 or day<1):
                continue
            print(f"{year}-{month:02}-{day:02}")
            break
    except(IndexError, ValueError):
        continue

            
            

