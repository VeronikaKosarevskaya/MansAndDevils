from game import homes, output, load


class Game:

    @staticmethod
    def game(first_enter):
        if first_enter:
            realHome = homes.Homes.home()
        else:
            realHome = homes.Homes.realHome
        myHome = homes.Homes.get_home(Game.get_numbers('Enter your numbers'))
        counter_name_1 = 0
        counter_name_2 = 0
        for real_position, real_number in realHome.items():
            for my_position, my_number in myHome.items():
                if real_position == my_position:
                    if real_number == my_number:
                        counter_name_1 += 1
                        break
                    else:
                        if real_number == my_number:
                            counter_name_2 += 1
                            break
                else:
                    if real_number == my_number:
                        counter_name_2 += 1
                        break
        counter_name_3 = 4 - counter_name_1 - counter_name_2
        toOutput = output.Output('Блатных', 'Мужиков', 'Чертей', counter_name_1, counter_name_2, counter_name_3)
        result = output.Output.get_output(toOutput)
        print(realHome)
        print(result)
        if counter_name_1 != 4:
            text = str(myHome)
            load.Load.write(text)
            Game.game(False)
        else:
            text = str(myHome)
            load.Load.write(text + '\n')
            output.Output.end()

    @staticmethod
    def get_numbers(text):
        print(text)
        num_1 = int(input('1я'))
        num_2 = int(input("2я"))
        num_3 = int(input("3я"))
        num_4 = int(input("4я"))
        values = Game.is_value(num_1, num_2, num_3, num_4)
        return values

    @staticmethod
    def is_value(num_1, num_2, num_3, num_4):
        if num_1/10 >= 1 or num_2/10 >= 1 or num_3/10 >= 1 or num_4/10 >= 1:
            return Game.get_numbers('Invalid length of numbers. Numbers must be from 0 to 9')
        elif num_1 == num_2 or num_1 == num_3 or num_1 == num_4 or num_2 == num_3 or num_2 == num_4 or num_3 == num_4:
            return Game.get_numbers('numbers must be unique')
        else:
            my_numbers = (num_1, num_2, num_3, num_4)
        return my_numbers
