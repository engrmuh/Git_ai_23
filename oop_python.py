# GIT VERSION LEARNING 
# FOSE Muhammad Umer Haroon
class Smile_Bot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi there! I'm {self.name}. What's your name?"

    def compliment(self):
        return "You have a smile that can make me lol!"

    def respond(self, message):
        if "hello" in message.lower():
            return self.greet()
        elif "thank you" in message.lower():
            return "You're welcome! But honestly, it's hard not to compliment you."
        else:
            return "Tell me more about yourself!"


if __name__ == "__main__":
    smiley = Smile_Bot("talk")

    print(smiley.greet())
    
    user_name = input("Your name: ")
    print(f"Nice to meet you, {user_name}!")

    while True:
        user_message = input("You: ")
        if user_message.lower() in ["exit", "quit"]:
            print("smiley: Catch you later :)!")
            break
        response = smiley.respond(user_message)
        print(f"smiley: {response}")
