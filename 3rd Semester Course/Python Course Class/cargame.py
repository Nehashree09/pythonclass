command=" "
started= False
while command.lower()!= quit:
    command=input("> ")
    if command=="start":
        if started:
            print("car already started")
        else:
            started=True
            print("car started...ready to go!")
    elif command=="stop":
        if not started:
            print("car already stopped")
        else:
            stopped =True
            print("car stopped ")
    elif command=="help":
        print("""
 start-to start the car
 stop-to stop the car
 quit-to end the game
        """)
    elif command=="quit":
        break
    else:
        print("i do not understand")