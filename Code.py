import time
import pywhatkit as pwt
import webbrowser as wb


def surl():
    return "\u001b[32;1m" + "Searching URL..."


print("\u001b[34m" + "Hello, How Can I Help You?")

Command = input("\u001b[97m" + "Hey,")

if Command == "Time":
    print("\u001b[33;1m" + "Checking Local Time...")
    time.sleep(1)
    print("\u001b[33;1m" + "Current Time:")
    Time = time.strftime("%I:%M %p")
    time.sleep(0.8)
    print(Time)


elif Command == "Open Youtube":
    URL = "https://www.youtube.com/"
    time.sleep(2)
    print(surl())
    time.sleep(1)
    print("\u001b[32;1m" + "Opened URL'https://www.youtube.com/'")
    print("\u001b[32;1m" + "Playing...")
    wb.open(URL)

elif Command == "Play Music":
    music = input("Name ")
    time.sleep(2)
    print("\u001b[33;1m" + "Redirecting...")
    print("\u001b[33;1m" + "Playing")
    time.sleep(1)
    pwt.playonyt(music)

elif Command == "Open Github":
    URL_G = "https://github.com/"
    wb.open(URL_G)
    print(surl())

elif Command == "Search Video":
    music = input("Search,")
    time.sleep(2)
    print("\u001b[33;1m" + "Redirecting...")
    time.sleep(1)
    pwt.playonyt(music)

elif Command == "Calculate":
    N1 = input("\u001b[4m" + "Digit 1,")
    N2 = input("\u001b[4m" + "Digit 2, ")

    N1 = float(N1)
    N2 = float(N2)

    Op = input("\u001b[35;1m" + "Operation,")

    if Op == "+":
        print(N1 + N2)  # <---- ADDITION
    elif Op == "-":
        print(N1 - N2)  # <-----SUBTRACTION
    elif Op == "*":
        print(N1 * N2)  # <-----MULTIPLICATION
    elif Op == "/":
        print(N1 / N2)  # <-----DIVISION
    elif Op == "//":  # ADVANCED CALCULATIONS
        print(N1 // N2)  # <-----FLOOR DIVISION
    elif Op == "**":
        print(N1 ** N2)  # <-----EXPONENT
    elif Op == "%":
        print(N1 % N2)  # <-----MODULUS
    else:
        print("Maybe Try Something in my capabilities?")
        print("Operations:- + , - , * , / , // , ** ,% ")
