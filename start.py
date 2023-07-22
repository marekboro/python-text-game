# Global variables
playerName =''
randomOptions = ["a. You try to open the door","b. You look for a light switch","c. You listen to any sounds","d. You try to smell"]
roomDescriptions = ['The room is dark, there are no sounds to be heard']

class Room:
    def __init__(self, introduction:str, questionsArray:list[str]):
        self.introduction = introduction
        self.questionsArray = questionsArray

def main():
    initGame()
    runSpecificRoom(room1)

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

def runSpecificRoom(room:Room):
    print(room.introduction)
    # print("------------------------------------------")
    # print(separator(room.introduction))
    # chosenOption = get_choice(getListStringFromArray(room.questionsArray))
    chosenOption = get_choice(getListStringFromRoom(room))
    print(f"{playerName} chose {chosenOption}")


# def get_choice_for_room(room:Room):
    
#     return get_choice(getListStringFromRoom(room))
    

def getListOfChoices():
    return "a. You try to open the door\nb. You look for a light switch\nc. You listen to any sounds\nd. You try to smell\n"

def getListStringFromRoom(room:Room):
    string = f"{separator(room.introduction)}\n"
    for entry in room.questionsArray:
        string +=f"{entry}\n"
    return string

def getListStringFromArray(array):
    string = ''
    for entry in array:
        string +=f"{entry}\n"
    return string

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

def separator(text:str):
    chars = ""
    for character in text:
        chars +="-"
    return chars
room1 = Room(roomDescriptions[0],randomOptions)
          
main()

# room generator
# # some things in rooms hidden, unlocked by actions
# # items randombly spread around maze
# # special items needed to exit maze
# # no death, just mystery getting out.
