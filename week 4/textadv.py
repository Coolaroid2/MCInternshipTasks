#text-based adventure game
print("\t\t\t----------Text-Based Adventure Game----------")
print("\nYou arrive at your new nightshift job at a local pizza place, called Freddy Fazbear's Pizza.\nThe food there is decent, but the main attraction of this particular location are the animatronics.\nThey are robot figures that are programmed to move in certain patterns to emulate them being alive.\nThey have the builds of adult humans but with the heads of robotic animals.\nThey're called Freddy, Bonnie, Chica, and Foxy with the heads of a bear, a bunny, a chicken, and a fox respectively.\nYou heard that the last security guard met with an accident and had to quit the job.\nThe details weren't shared.\n\nTime -> 12:00 AM\nYou clock in and sit down at your desk, ready to watch the security monitors until you get off of work at 6:00 AM.\nIn the main hall, the animatronics are lined up Freddy, Bonnie, Chica and Foxy left to right.\n")

def scene():
    print('Make a choice:\n1. Stay in the monitor room.\n2. Get a snack from the vending machine outside\n')
    while True:
        try:    
            ch1 = input('What do you want to do? (Enter 1 or 2): ')
            if int(ch1) == 1:
                scene1()
                break
            elif int(ch1) == 2:
                scene2()
                break
            else:
                print('Please enter a valid option')
        except:
            print('Please enter a valid option')

def scene1():
    print('\nTime -> 1:00 AM\nYou choose to stay in the monitor room.\nAfter some time has passed, you notice something odd.\nBonnie has disappeared from the main hall.\nYou check the cameras in the other rooms and you find Bonnie standing in the dining hall, looking straight into the camera.\nHow could this be?')
    print('\nMake a choice:\n1. Stay in the monitor room.\n2. Go investigate\n')
    while True:
        try:    
            ch1 = input('What do you want to do? (Enter 1 or 2): ')
            if int(ch1) == 1:
                scene1_1()
                break
            elif int(ch1) == 2:
                print('You walk out of the monitor room and enter the dining hall with you flashlight.\nBonnie is nowhere to be seen.\nSuddenly a chill runs down your spine as you look down and see a shadow slowly enveloping your own.\nYou turn around and are met face to face with Bonnie.\nHe attacks you and shreds you to pieces.\nYOU LOSE\nTHE END.')
                break
            else:
                print('Please enter a valid option')
        except:
            print('Please enter a valid option')

def scene1_1():
    print('\nTime -> 2:00 AM\nYou choose to stay in the monitor room.\nBonnie has moved once again, this time to the hallway out the left side of your room.')
    print('\nMake a choice:\n1. Close the left door and stay in the monitor room.\n2. Take your flashlight and check it out\n')
    while True:
        try:    
            ch1 = input('What do you want to do? (Enter 1 or 2): ')
            if int(ch1) == 1:
                scene1_1_1()
                break
            elif int(ch1) == 2:
                print('You open the door a bit to look into the hall.\nThe flashlight was refusing the cooperate but turned on after a few tries, and when you pointed it into the hall, you were met with Bonnie, right in front of your face.\nHe attacks you and rips you to shreds.\nYOU LOSE\nTHE END.')
                break
            else:
                print('Please enter a valid option')
        except:
            print('Please enter a valid option')

def scene1_1_1():
    print('\nTime -> 3:00 AM\nYou choose to stay in the monitor room.\nYou go and close the left door.\nYou lean in to the door to hear if there are any noises outside.\nA raspy heavy breathing can be heard right next to the door.\nYou keep the door tightly shut until you hear Bonnie slowly walking away.')
    print('\nMake a choice:\n1. Go back to your desk and keep monitoring.\n2. Take your flashlight and go after him\n')
    while True:
        try:    
            ch1 = input('What do you want to do? (Enter 1 or 2): ')
            if int(ch1) == 1:
                scene1_1_1_1()
                break
            elif int(ch1) == 2:
                print('What is happening?\nConfused, you decide to go after him.\nNot sure where to go, you enter the dining hall where you first saw Bonnie.\nInstead of Bonnie however, youre met with Freddy entering the room from the door on the opposite side of the room which leads to the main hall.\nYou freeze in place but he had already notcied you.\nFreddy leaps over to you and consumes you.\nYOU LOSE\nTHE END.')
                break
            else:
                print('Please enter a valid option')
        except:
            print('Please enter a valid option')

def scene1_1_1_1():
    print('\nTime -> 4:00 AM\nYou choose to stay in the monitor room.\nChica has now gone missing from the main hall as well.\nYou find her in the kitchen, slyly standing in the corner minding her own business.')
    print('\nMake a choice:\n1. Stay in the monitor room.\n2. Take your flashlight and check it out\n')
    while True:
        try:    
            ch1 = input('What do you want to do? (Enter 1 or 2): ')
            if int(ch1) == 1:
                scene1_1_1_1_1()
                break
            elif int(ch1) == 2:
                print('You decide to go check it out.\nThe flashlight came in handy as you navigated your way through the rooms until you reached the kitchen.\nSlowly, you turn the door handle and walk in, carefully looking at the surroundings with your flashlight as you do so.\nThere, in the same corner you saw her in the monitor, you see Chica standing perfectly still.\nYou go over slowly to inspect as she didnt seem to be active.\nHowever, as you walk closer, you notice her eyes.\nThey were following you the whole time.\nYou got careless.\nSuddenly, Chica lunges at you and tears you to pieces.\nYOU LOSE\nTHE END.')
                break
            else:
                print('Please enter a valid option')
        except:
            print('Please enter a valid option')

def scene1_1_1_1_1():
    print('\nTime -> 5:00 AM\nYou choose to stay in the monitor room.\nYou thoroughly check the cameras and find that Freddy is now missing as well.\nYou find him in the hallway out the left side of your room.\nChica has also closed in and is in the hallway out the right side of your room.')
    print('\nMake a choice:\n1. Close the left door and stay in the monitoring room.\n2. Close the right door and stay in the monitoring room.\n3. Hide in the corner of the room.\n')
    while True:
        try:    
            ch1 = input('What do you want to do? (Enter 1 or 2 or 3): ')
            if int(ch1) == 1:
                print('You get up and close the left door.\nFreddys breaths can be hear outside, and he was not backing away.\nSuddenly you hear heavy footsteps rapidly approaching from the right hallway to which the door you left open.\nOut of fear you run across the room and close the right door.\nHowever, in that moment, Freddy rushes through the left door and consumes you.\nYOU LOSE.\nTHE END.')
                break
            elif int(ch1) == 2:
                print('You get up and close the right door.\nChicas breaths can be hear outside, and she was not backing away.\nSuddenly you hear heavy footsteps rapidly approaching from the left hallway to which the door you left open.\nOut of fear you run across the room and close the left door.\nHowever, in that moment, Chica rushes through the right door and tears you to pieces.\nYOU LOSE.\nTHE END.')
                break
            elif int(ch1) == 3:
                print('You rush to hide in a dark corner of the monitor room.\nSounds of footsteps from both hallways get closer and closer.\nSlowly, Freddy and Chica poke their heads into the room.\nThey look around, trying to find any trace of you.\nYou sit there holding your breath so that you dont make any noise.\nThe animatronics walk around the room, treading softly.\nChica walks in your direction and freezes when shes a few feet away.\nShe could smell you.\nFreddy turns your way as well.\nIn the distance you hear more footsteps, and in a few seconds, Bonnie and Foxy rush into the room.\nThey all start closing in on you.\nIts over.\nSuddenly, a small alarm starts ringing from your desk.\nAll the animatronics froze.\nYou look over at the clock.\nIts 6:00 AM.\nThe animatroincs turn around and walk out of the room, leaving you alone.\nYour shift was over.\nYou survived the night.\nTHE END')
                break
            else:
                print('Please enter a valid option')
        except:
            print('Please enter a valid option')

def scene2():
    print('\nTime -> 1:00 AM\nYou go to the vending machine and get a snack, but hear a weird noise coming from the main hall.')
    print('\nMake a choice:\n1. Go back to the monitor room.\n2. Go investigate\n')
    while True:
        try:    
            ch1 = input('What do you want to do? (Enter 1 or 2): ')
            if int(ch1) == 1:
                scene1()
                break
            elif int(ch1) == 2:
                print('You enter the main hall and see nothing out of the ordinary.\nFreddy, Bonnie and Chica are all standing where they should be and all is well...\nWhere is Foxy?\nYou hear a metallic growl coming from above you.\nFoxy pounces down from the ceiling and devours you.\nYOU LOSE\nTHE END.')
                break
            else:
                print('Please enter a valid option')
        except:
            print('Please enter a valid option')

scene()