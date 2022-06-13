class Load:
    flag = True
    content = []

    @staticmethod
    def write(text):
        with open('Game.txt', 'a') as file:
            if Load.flag:
                file.write('Document of game\n')
                Load.flag = False
            file.write(text)

    @staticmethod
    def read():
        with open('Game.txt', 'r') as file:
            Load.content = file.read()
