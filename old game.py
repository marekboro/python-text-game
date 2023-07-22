# Global variables
playerName =''


def main():
    print(room1.introduction)
    print(room1.questionsArray)
    # initGame()
    # runRoom()

def askPlayerName():
    global playerName
    playerName = input("Please enter your name: ")

def enterRoom():
    global playerName
    print(f"{playerName} enterd the room")
    print("The door closed behind you")

def initGame():
    askPlayerName()
    enterRoom()


def runRoom():
    print("The room you are in is dark")
    chosenOption = get_choice(getListOfChoices())
    print(f"{playerName} chose {chosenOption}")



def getListOfChoices():
    return "a. You try to open the door\nb. You look for a light switch\nc. You listen to any sounds\nd. You try to smell\n"
    

def get_choice(prompt):
    while(True):
        try:
            selected = input(prompt)
            if input_valid(selected):
                return selected
        except:
            continue

def input_valid(choice:str):
    return choice == "a" or choice == "b" or choice =="c" or choice =="d"



class Room:
    def __init__(self, introduction, questionsArray):
        self.introduction = introduction
        self.questionsArray = questionsArray

        # introd:str,
        # questions:str[],
room1 = Room("dsds",["a","b"])
          
main()

# room generator
# # some things in rooms hidden, unlocked by actions
# # items randombly spread around maze
# # special items needed to exit maze
# # no death, just mystery getting out.
