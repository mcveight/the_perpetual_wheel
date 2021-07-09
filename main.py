import os
load = open('load.txt', 'a')

# executes decisions based in the load.txt file
class load(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def check(self):
        var = open('load.txt', 'r')
        var2= var.readline()
        if var2 != self.a:
            var3 = open('load.txt', 'a')
            var3.write(self.a)
            print(self.b)
        elif var2 == self.a:
            print('rm')

def game():
    print(" The life it's a loop,\n all are condemned to repeat their actions again and again,\n a perpetual wheel... until they're decided to change something.\n You are a prisoner, a prisoner of the twist, have a good luck cliche hero to achieve your goal")
    name = input('By the way what is your name cliché hero?')
def start():
    d = input("Hey open your eyes, it's time to start your cliché hero adventure!\n 1) Open your eyes\n 2) leave\n")

    if d == '1':
        game()
    else:
        leaveChoice = load('the player decided leave', 'end...')
        leaveChoice.check()

start()
