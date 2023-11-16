
print ("Welcome to Treasure island.\n")
print("Your mission is to find the treasure.\n")
direction = input("You are at cross road , where you want to go ? left or right").lower()
if direction == "left" or direction == "LEFT":
    action = input("You come to a lake there is a island in middle of the lake.Type 'wait' to wait for boot or 'swim' to swim:\n")
    if action == "wait" or action == "WAIT":
        door= input("You have arrived at island safely, you need to choose one door . option 'blue','red','yellow'")
        if door == "blue" or door == "BLUE":
            print('''Eaten by beasts.
              Game Over.''')
        elif door == "yellow" or door =="YELLOW":
            print("You Win !")
        elif door == "red" or door == "RED":
            print('''Burned by fire.
                Game Over.''')
        else:
            print("*** Game Over ***")
    else:
        print('''Attacked by trout.
        Game Over.''')
else:
    print('''Fall into a hole.
    Game Over''')