g = {}
count = 0
while True:
    try:
        answer = input("Whats ur grocery? ").strip().lower()
        if answer in g:
            g[answer] = g[answer]+1
            continue
        else:
            g[answer] = 1
            continue
    except(EOFError):
        break


for i in sorted(g):
    print(f"{g[i]} {i.upper()}")


        