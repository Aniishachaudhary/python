print("""Stop! Who would cross the Bridge of Death \nMust answer me these questions three, 'ere the other side he see.\n""") 
user_name=input("What is your name? ")
if (user_name.capitalize()!= "Arthur"): #It capitalize the name Arthur
    seek=input("What do you seek?")
    if "grail" in seek.lower(): # Checking for grail in answer
        colour=input("What is your favourite colour?")
        if user_name.capitalize()[0]==colour.capitalize()[0]: #It checks first alphabet of name and colour
            print("You may pass!")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
    else:
        print("Only those who seek the Grail may pass.")
else:
    print("My liege! You may pass!")