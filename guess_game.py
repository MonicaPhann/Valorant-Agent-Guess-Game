import random

fileOpen = open("champs.csv", "r")
#read = fileOpen.readline().strip().split(",")
nameList = []
roleList = []
countryList = []


for line in fileOpen:

    line = line.strip("\n").split(",")
    nameList.append(line[0])
    roleList.append(line[1])
    countryList.append(line[2])

user = input("Guess the Agent!\n").lower().capitalize()

def hint (tries):
    if tries == 0:
        print("Hint!!!! Role is:",roleList[randInt],"\n")
    elif tries == 1:
        print("Hint!!!! From:",countryList[randInt],"\n")

def find (name,agent):
    x = True
    attempt = 0
    while x:
        
        if name == agent:
            print("\nYou have guessed the correct agent! The agent was:", agent,"\n")
            x = False

        elif name != agent and name in nameList:
            print( "\nWrong! Try again.")
            hint(attempt)
            name = input("Guess the Agent!\n").lower().capitalize()

            attempt = attempt + 1
            
        elif name not in nameList:
            print("\nUh oh! This is not an agent name. Try again!")
            name = input("Guess the Agent!\n").lower().capitalize()

randInt = random.randrange(0,len(nameList))

find(user,nameList[randInt])
