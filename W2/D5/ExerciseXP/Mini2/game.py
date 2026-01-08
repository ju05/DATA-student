import random


class Game:

    @staticmethod
    def item_dict(number_to_item):
        game_dict = {1:"rock", 2:"paper", 3:"scissors"}
        return game_dict[number_to_item]

    def get_user_item(self):
        while True:
            user_choice = input("Please choice the item for turn (1 - rock, 2 - paper, 3 - scissors): ").strip()
            if not user_choice.isnumeric():
                print("You should input only number!")
            elif int(user_choice) in (1, 2, 3):
                return int(user_choice)
            else:
                print("You don't have so much choices!")

    def get_computer_item(self):
        return random.randint(1, 3)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        if computer_item-user_item in (1, -2):
            return "loss"
        else:
            return "win"

    def play(self):
        user_turn = self.get_user_item()
        computer_turn = self.get_computer_item()
        result = self.get_game_result(user_turn, computer_turn)
        print(f"{self.item_dict(user_turn)}, {self.item_dict(computer_turn)}, {result}")
        return result
