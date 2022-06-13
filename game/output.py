from game import load


class Output:

    def __init__(self, name_1, name_2, name_3,
                 counter_name_1, counter_name_2, counter_name_3):
        self.name_1 = name_1
        self.name_2 = name_2
        self.name_3 = name_3
        self.counter_name_1 = counter_name_1
        self.counter_name_2 = counter_name_2
        self.counter_name_3 = counter_name_3
        if counter_name_1 == 1:
            self.name_1 = 'Блатной'
        if counter_name_2 == 1:
            self.name_2 = 'Мужик'
        if counter_name_2 > 1:
            self.name_2 = 'Мужика'
        if counter_name_3 == 1:
            self.name_3 = 'Чёрт'
        if counter_name_3 > 1:
            self.name_3 = 'Чёрта'

    def get_output(self):
        output = f'{self.counter_name_1} {self.name_1}, {self.counter_name_2} {self.name_2}, ' \
                 f'{self.counter_name_3} {self.name_3}'
        return output

    @staticmethod
    def end():
        end = "You won! Congratulations!"
        # moves = load.Load.read()
        # return print(end), moves
        return end
