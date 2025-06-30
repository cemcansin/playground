room_num = 10
xp = 0

    









print("Hello traveller ! \nPlease tell me about yourself \nAre you a warrior, a mage or a rogue")
choice = input()
if choice == ("warrior"):
    print("A mighty warrior !")
if choice == ("mage"):
    print("A wise mage")
if choice == ("rogue"):
    print("So you are a stone cold assassin")
else:
    print(str(choice) + (", interesting"))
print("Here you have a dungeon, what would you like to do \nYou can move, attack or check status \nWhile moving you can choose to go left or right \nFor now, lets move")
choice = input()
if choice == "left":
    print("going left")
    room_num = room_num - 1
    if room_num == 9:
        enemy_count = 1
        if enemy_count >= 1:
                print("encountred an enemy \nYou have to attack to continue")
                choice = input()
                if choice == "attack":
                    print("Slained an enemy \nGained 2xp")
                    enemy_count = enemy_count - 1
                    xp = xp + 2
                else :
                    print("died \n Game Over !")
        
    
if choice == "right":
    print("going right")
    room_num = room_num + 1
    if room_num == 11:
        print("you have found treasure !")
        xp = xp + 6
if xp >= 2:
        print("lets move to a different room")        




