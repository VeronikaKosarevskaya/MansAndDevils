class Homes:

    realHome = {}

    def __init__(self, first_number, second_number, third_number, fourth_number):
        self.first_number = first_number
        self.second_number = second_number
        self.third_number = third_number
        self.fourth_number = fourth_number

    def get_home(self):
        return {1: self.first_number, 2: self.second_number, 3: self.third_number, 4: self.fourth_number}

    @staticmethod
    def home():
        import random
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        first_number = numbers[random.randint(0, 9)]
        numbers.remove(first_number)
        second_number = numbers[random.randint(0, 8)]
        numbers.remove(second_number)
        third_number = numbers[random.randint(0, 7)]
        numbers.remove(third_number)
        fourth_number = numbers[random.randint(0, 6)]
        realHome = {1: first_number, 2: second_number, 3: third_number, 4: fourth_number}
        Homes.realHome = realHome
        return realHome
