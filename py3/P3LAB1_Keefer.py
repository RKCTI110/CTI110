# CTI 110
# P3LAB1 - Choose your own adventure
# KeeferR
# 10/22/24
 
def main():
    print("This better work") 
    go_home()
    front_door()

def go_home():
    print("You decide to go home.")
    print("But you should get some food?")
    print("1. Order Pizza")
    print("2. Get Chinese")
    choice = int(input())
    if choice == 1:
        get_pizza()
    if choice == 2:
        get_chinese()

def get_pizza():
    print("Pizza arrives, pizza box opens and pulls you into wormhole")
    print("You appear at the front door of a haunted house 👻")

def get_chinese():
    print("Chinese delivery guy arrives then kills you")
    print("💀💀💀💀 BAD ENDING 💀💀💀")

def front_door():
    print("The front door is slightly open.")
    print("Should you knock first, or just push the door open?")
    print("1. Knock")
    print("2. Push door open")
    choice = int(input())
    if choice == 1:
        knock()
    if choice == 2:
        push_open()

def knock():
    print("The door slowly and loudly opens")
    print("You have safely gained access to the house")

def push_open():
    print("A shadow figue grabs you, pulling you in")
    print("You have awoken in the basement")


# start the program
main()