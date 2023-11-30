play = input("Do you want to start your Adventure Y/N? ")
while play.lower() == "y":
    wake_up = input('''You awake to find yourself in a dark room with chains on your ankles. In your pockets you have your PHONE a box of MATCHES and your CAR KEYS. ''').lower()
    while wake_up == "phone":
        phone = input('''Your phone has no service and only enough battery to use the FLASHLIGHT for 3 minutes. You still have the MATCHES and CAR KEYS if you want to save your phone battery.''').lower()
        if phone == "flashlight":
            flashlight = input('''You use your phones flashlight to look around. You spot a SAW near the pipe that your chain is attached to. You also see an open TOOL BOX that you can reach.''').lower()
            if flashlight == "saw":
                door_window_answer = input('''You sawed through the pipe and can now move around the room you see a DOOR and a WINDOW.''').lower()
                if door_window_answer == "door":
                    print('''You open the door to find a man in a pig mask holding you at gun point. you hear hysterical laughter then everything goes dark''')
                    play = 'done'
                    wake_up = 'done'
                    break
                elif door_window_answer == "window":
                    print('''You pull yourself up opening the window and crawling out onto the dirt as you do your phone dies and you are left in complete darkness. Only the stars are avaliable to guide you back home. Good Luck HE'S COMING FOR YOU.''')
                    play = "done"
                    wake_up = 'done'
                    break
                else:
                    wake_up = 'l'
                    break
            elif flashlight == "tool box":
                tool_box = input('''In the tool box you see a KEY RING with 5 keys and a HAMMER. ''')
                if tool_box.lower() == 'key ring':
                    key_ring = input('''You unlock your chains with one of the keys. Looking around the room you can grab the HAMMER or LEAVE through the door.''')
                    if key_ring.lower() == 'hammer':
                        print('''Grabbing the hammer you head out the door and up stairs you reach a locked door. Using the key ring you open the door you find a person in a pig mask. On instinct you swing the hammer
                               and silence falls as the body does.''')
                        play = 'win'
                        wake_up = 'done'
                        break
                    elif key_ring.lower() == 'leave':
                        print('''As you head up the stairs you hear a sound coming from your right you look and see a vent. Moving closer you can tell that the sound is hysterical laughter.
                               Everything goes dark.''')
                        play = 'done'
                        wake_up = 'done'
                        break
                    else:
                        wake_up = 'l'
                        break
                elif tool_box.lower() == 'hammer':
                    hammer = input('You are able to smash the lock off your leg with the hammer but in the process it breaks you can grab the KEY RING or LEAVE through the door')
                    if hammer.lower() == 'key ring':
                        print('''You turn around to grab the key and start to get up but you suddenly feel woozy, Everything goe black.''')
                        play = 'done'
                        wake_up = 'done'
                        break
                    elif hammer.lower() == 'leave':
                        print('''You start to leave opening the door and heading up the stairs, but you find a locked door at the top. You start to head back to get the key ring when suddenly you feel a push from behind.
                               Everything goes dark.''')
                        play = 'done'
                        wake_up = 'done'
                        break
                    else:
                        wake_up = 'l'
                        break
                else:
                    wake_up = 'l'
                    break
            else:
                wake_up = 'l'
                break
        elif phone == "matches":
            wake_up = "matches"
            break
        elif phone == "car keys":
            wake_up = "car keys"
            break
        else:
            wake_up = 'l'
            break
    while wake_up == "matches":
        matches = input("Your box of matches has 10 MATCHES that will last 30 seconds each alternativley you have your PHONE and CAR KEYS still.").lower()
        if matches == 'matches':
            matches2 = input('''You strike your first match and can see that your shackles are not attached to anything you must choose a direction to explore
                              FORWARD, RIGHT, or LEFT.''')
            if matches2.lower() == 'forward':
                forward = input('''You come upon a door and try the handle opening it you see a dark hallway walking to the top you find yourself in a small cabin
                                 there is an AXE laying on one side of the room and a DOOR on the other.''')
                if forward.lower() == 'axe':
                    print('As you grab the axe you hear a loud bang and fall over. everything goes black.')
                    play = 'dead'
                    wake_up = 'done'
                    break
                elif forward.lower() == 'door':
                    door = input('As you walk outside you see that you have two optiond walk down a dirt ROAD to find a way out or try to run through the WOODS')
                    if door.lower() == 'road':
                        print('As you begin to walk down the road you see a pair of headlights coming at you. Hoping for some help you run at the car and wave your arms. The car speeds up right at you, you hear laughing. everything goes dark')
                        play = 'dead'
                        wake_up = 'done'
                        break
            elif matches2.lower() == 'right':
                right = input('you find a wall covered in photos of you in your bed, at work, and even on your trips out of state. you turn to run only to see a person in a pig mask. everything goes black. ')
                play = 'dead'
                wake_up = 'done'
                break
            elif matches2.lower() == 'left':
                left = input('You come to find a WINDOW you can crawl out of and a KNIFE you can pick up.')
                if left.lower() == 'window':
                    print('As you crawl out of the window you pull your phone out of your pocket and find that you have service. You call the police and hide. 15 minutes later you hear the sirens.')
                    play = 'win'
                    wake_up = 'done'
                    break
                elif left.lower() == 'knife':
                    print('You lean over to pick up the knife and feel a prick in your neck. everything goes dark.')
                    wake_up = 'done'
                    break
                else:
                    wake_up = 'l'
                    break
            else:
                wake_up = 'l'
                break
        elif matches == 'phone':
            wake_up = 'phone'
            break
        elif matches == 'car keys':
            wake_up = 'car keys'
            break
        else:
            wake_up = 'l'
            break
    while wake_up == "car keys":
        car_keys = input("you pull out your car keys and try to pick the lock on your ankle but fail the key doesnt fit you still have your PHONE and MATCHES.").lower()
        if car_keys == 'phone':
            wake_up = 'phone'
            break
        elif car_keys == 'matches':
            wake_up = 'matches'
            break
        else:
            wake_up = 'l'
            break
    if wake_up == 'done':
        break
    else:
        print("Item not recognized.")
        play = 'restart'
        break
if play.lower() == "n":
    print("Then why are you here? LEAVE")
if play.lower() == "dead":
    print('BEHIND YOU')
if play.lower() == 'win':
    print('Congratulations! You Survived')
if play.lower() == 'restart':
    print('Restart.')