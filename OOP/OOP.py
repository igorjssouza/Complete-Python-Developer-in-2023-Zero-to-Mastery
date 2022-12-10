class PlayerCharacter:
    # Static class
    membership = True
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def run(self):
        print("run")
        return 'done'

    def shout(self):
        return f'My name is {self.name}'


player1 = PlayerCharacter("Cindy", 33)
player2 = PlayerCharacter("Tom", 40)

player2.attack = 50

print(player1.shout())
print(player2.shout())
