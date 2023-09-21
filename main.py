class User():
    def __init__(self):
        self.name = ""
        self.age = 0

    def setName(self, nameI):
        self.name = nameI

    def setAge(self, ageI):
        self.age = ageI

class ChatBot():
    def __init__(self):
        self.serviceNum = ""
        self.NewUser = User()
        print("Welcome to the Elite 101 Chatbot")
        self.NewUser.setName(input("What is your name? "))
        while True:
            try:
                self.NewUser.setAge(int(input("What is your age? ")))
                break
            except ValueError:
                print(self.NewUser.name, ", That was an invalid input, please enter a valid age.")
        print(self.NewUser.name, ", How can I help you today?")
        self.reqServiceNum()

    def service(self):
        if self.serviceNum == 1:
            print("Serv 1")
        elif self.serviceNum == 2:
            print("Serv 2")
        elif self.serviceNum == 3:
            print("Serv 3")

    def reqServiceNum(self):
        while True:
            try:
                self.serviceNum = int(input("Type a number in for which service you would like \n \
                    1. PlaceHolder 1 \n \
                    2. PlaceHolder 2 \n \
                    3. PlaceHolder 3 \n \
                    4. End the conversation \n"))
                if 1 <= self.serviceNum <= 4:
                    break
                else:
                    print("Invalid choice. Please choose a number between 1 and 4.")
            except ValueError:
                print(self.NewUser.name,", You must input an integer!")
   
    def getServiceNum(self):
        return self.serviceNum

def main():
    chatbot1 = ChatBot()
    while chatbot1.getServiceNum() != 4:
        chatbot1.service()
        chatbot1.reqServiceNum()
    print("Thanks for using this chatbot")

main()