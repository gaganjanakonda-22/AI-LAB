def laptop(turn_on,internet_work,is_slow):
    if turn_on=="no":
         return"please check the charger and power cable."
    elif internet_work=="no":
        return"please check the wifi & re start the router."
    elif is_slow=="yes":
        return"please close the unsend program and restart the laptop."
    else:
        return"The system does not find a common problem."

turn_on=input("Does laptop turn on ? (yes/no) : ").lower()
internet_work=input("Does the internet work ? (yes/no):").lower()
is_slow= input("Is the laptop slow ? (yes/no):").lower()
advice= laptop(turn_on,internet_work,is_slow)
print("\n--> Expert system advice:")
print(advice)