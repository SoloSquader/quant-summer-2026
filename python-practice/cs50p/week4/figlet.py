import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv)==1:
    chosen = random.choice(fonts)
    figlet.setFont(font = chosen)
    text = input("Text? ")
    hehe = figlet.renderText(text)
    print(hehe)
elif len(sys.argv)==3:
    if sys.argv[1]!="-f" and sys.argv[1]!="--font":
        sys.exit("stop.")
    elif sys.argv[2] not in fonts:
        sys.exit("invalid")
    else:
        figlet.setFont(font = sys.argv[2])
        text = input("text? ")
        obj = figlet.renderText(text)
        print(obj)
else:
    sys.exit("invalid")
        