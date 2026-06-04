total = 0
while True:
    try: 
        dict = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
        
        answer = input("Whats ur order? ").strip().lower().title()
        total = total+dict[answer]
        print(f"your total is: ${total:.2f}")
        continue

    except(EOFError):
        print(f"your total is ${total:.2f}")
        break
    
    except(KeyError):
        continue
    

    