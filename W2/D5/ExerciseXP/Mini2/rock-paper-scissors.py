from game import Game


def get_user_menu_choice():
    while True:
        user_decision = input("1) Play a new game\n2) Show scores\n3) Quit\nWhat is your choice: ").strip()
        if not user_decision.isnumeric():
            print("You should input only number!")
        elif int(user_decision) in (1, 2, 3):
            return int(user_decision)
        else:
            print("You don't have so much choices!")


def print_results(results):
    print(f"Wins: {results['win']}, Losses: {results['loss']}, Draws: {results['draw']}")


def main():
    global results
    while True:
        user_think = get_user_menu_choice()
        if user_think == 3:
            print_results(results)
            print("Goodbye")
            break
        elif user_think == 1:
            game = Game()
            results[game.play()] += 1
        elif user_think == 2:
            print_results(results)


results = {"win": 0, "loss": 0, "draw": 0}
if __name__ == "__main__":
    main()
