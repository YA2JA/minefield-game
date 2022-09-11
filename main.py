import random
import numpy as np

from cli_args_system import Args

def gen_map():
    game_map = np.concatenate( 
                                (np.zeros(16).reshape((4, 4)), np.zeros(4).reshape((4, 1)) + 1 ),
                                axis=1
                            )
    np.apply_along_axis(np.random.shuffle, 1,  game_map) 
    return game_map

def game():
    game = gen_map()
    for id, line in enumerate(game):
        
        val = int(input("Please enter the value from 0 to 5: "))
        
        if (1 == line[val]):
            print("You lose !\n")
            print(game)
            return
        
        if (id == (len(game)-1)):
            print("You win")
            print(game)
            return

        print(f"You pass ! previs line look like this:{line} \n")
        with open("result.txt", "w+") as file:
            file.write(str(game))
            file.close()

def autopilot(number_match):
    win = lose = 0
    for i in range(number_match):
        game = gen_map()
        tries = [random.randint(0,4) for i in range(4)]
        for line, choise in zip(game, tries):
            if line[choise] == 1:
                lose += 1
                break
        if (lose+win) <= i:
            win += 1
    print(win, lose)
    
def main():
    args = Args(convert_numbers=True)

    help_flag = args.flag_str('h','help')
    auto_flag = args.flag_str('a','auto')
    game_flag = args.flag_str('g','game')

    if help_flag or not (auto_flag or game_flag):
        print("\nThis script which help you to understand all difficulty to estimate probability.",
            "\nThis script consiste into generate a small game, whiche sime to be long term winning,",
            "\nbut in fact you lose more, to test this you can launche an autopilote and plays as much as you",
            "\nwant parties fast.",
            """\nCommands:
                -h --help Show this help message and exit
                -a --auto Generate  number of games
                   -a [num]
                -g --game Start the game\n""")
    elif auto_flag:
        autopilot(auto_flag)
    
    elif game_flag:
        game()

if __name__ == "__main__":
    main()