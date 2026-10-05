print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")
print("_____________________________________")
print("____________ GOOD LUCK ______________")
print("_____________________________________\n\n\n")

print("You wake up alone on an island.\n"
      "You're dressed as a clown and your name tag reads 'DooKy'.\n"
      "Your journey begins...\n")

choice = input("do you go left or right? ").lower()
while choice != "right" and choice != "left":
    choice = input("nonsense is not an option, DooKy... left or right? ").lower()
if choice == "right":
    print("You fell into a hole. DooKy has died.")
elif choice == "left":
    choice = input("An explosion happens. You see a lake. A boat might come. Swim or wait? ").lower()
    while choice != "swim" and choice != "wait":
        choice = input("nonsense is not an option, DooKy...swim or wait? ").lower()
    if choice == "swim":
        print("Eaten by sharks. Game over, DooKy !")
    elif choice == "wait":
        choice = input("A boat comes and takes you across the river\n"
                       "Bears are coming\n"
                       "You see three doors: purple, yellow, and green.\n"
                       "which door do you choose? ").lower()
        while choice != "purple" and choice != "yellow" and choice != "green":
            choice = input("nonsense is not an option, DooKy... purple, yellow, or green? ").lower()
        if choice == "purple":
            print("You have small pox. DooKy has died.")
        elif choice == "yellow":
            print("You found the treasure - it's covered in black widows.\n"
                  "You freeze in fear.\n"
                  "The bears are here. They eat you. DooKy dies.")
        elif choice == "green":
            print("You enter the green door. You wake up at home.\n"
                  "You're 3 years old and blind with rage.\n"
                  "DooKy lives... but at what cost?")
print("\n  G A M E"
      "\n  O V E R"
      "\n D O O k Y")

