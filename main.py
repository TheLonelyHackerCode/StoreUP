print("Welcome To StoreUP v1")
input("Press Enter To Continue...")
print("The Game Where U HACK")
input("Press Enter To Continue...")
Diff = input("Difficulty: 1)Easy, 2)Medium, 3)Hard")
Name = input("Enter Your Hack Name: ")
print(Name + " Has Been Not Noticed Yet..")
Target = input("Enter The Target: ")
print("Aim " + Target + " Selected")
input("Press Enter To Continue...")
print("Hacking " + Target + "By" + Name + " Started")
input("Press Enter To Continue...")
# What To First Do
print("Options = 1)Shut Down Site, 2)Messege, 3)Ask For Money")
Action = input("What To First Do: [Number]")
if Action == "1":
    print("Shut Down " + Target + "'s Site?")
    input("Press Enter To Continue...")
    if Diff == "1":
        print("Easy Peacy Why?")
        input("Press Enter To Continue...")
        print("[1]Because Source Code On Github Free participation,[2]ccs and js stored in index.html [3]No 2FA")
        input("Press Enter To Continue...")
        StartWith = input("Start With?: [Number]")
        if StartWith == "1":
                startwithbut2 = input("Type Cd g:/github/repo/techbooboo" + Target)
                if startwithbut2 == "Cd g:/github/repo/techbooboo/" + Target:
                    Startwithbut3 = input("Type DIR DEL -gain admin rights")
                    if Startwithbut3 == "DIR DEL -gain admin rights":
                        print("Succsess")
                        input("Press Enter To Continue...")
                        print("10 YRS Ago")
                        input("Press Enter To Continue...")
                        print("Danger!" + Target + " Is Finding You!")
                        input("Lets Sign Out Of Social Media!")
                        print("Succsess")
                        print("You Won!")
                        input("Press Enter To Continue...")
                        print("Share This                           OMG I WON! :D in the hardest game with difficulty easy My Hack name is " + Name + "And My Target was" + Target + " :D                                                    Difficultly 2 Has More!")
                    else:
                        print("Failed (Game End)(" + Name + " Has Been Noticed)")
                else:
                    print("Failed (Game End)(" + Name + " Has Been Noticed)")        
        elif Diff == "2":
            print("Shut Down " + Target + "'s Site?")
            input("Press Enter To Continue...")
        elif Diff == "3":
            print("Shut Down " + Target + "'s Site?")
            input("Press Enter To Continue...")
elif Action == "2":
    print("Messege " + Target + "? ")
    input("Press Enter To Continue...")
elif Action == "3":
    print("Ask " + Target + " For Money?")
    input("Press Enter To Continue...")
else:
    print("Invalid Option")