import random
def dice_roll():
    roll = random.randint(1,6)
    print(roll)
name_pull = ["alex", "sabrina", "olaf", "jack"]
def pull():
    print(random.choice(name_pull))
dice_roll()
pull()
    
