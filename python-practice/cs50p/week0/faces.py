def main():
    name = input()
    print(convert(name))

def convert(to):
    to = to.replace(":)", "🙂")
    to = to.replace(":(", "🙁")
    return to

main()