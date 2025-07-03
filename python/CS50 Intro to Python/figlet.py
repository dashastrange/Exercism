from pyfiglet import Figlet
import sys

figlet = Figlet()
f_fonts = figlet.getFonts()

if len(sys.argv) ==3 or len(sys.argv) == 1:

    if len(sys.argv) == 3 and sys.argv[1] == '-f' and sys.argv[2] in f_fonts:
        text_input = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text_input))
    elif len(sys.argv) == 1:
        text_input = input("Input: ")
        print(figlet.renderText(text_input))
    else:
        sys.exit("Wrong args")

else:
    sys.exit("Wrong args")