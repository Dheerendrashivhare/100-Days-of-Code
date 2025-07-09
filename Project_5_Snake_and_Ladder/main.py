import random


def roll_dice():
    return random.randint(1, 6)


def Clc_Player_position(position, roll, board_size, snake, ladder):
    new_position = position + roll
    if new_position > board_size:
        return position
    else:
        if new_position in snake:
            new_position = snake[new_position]
            print(
                f"Oops you cought from sanke you get from {position} to {new_position}"
            )
        elif new_position in ladder:
            new_position = ladder[new_position]
            print(
                f"yehh you got ladder you get from {position} to {new_position}"
            )
        return new_position


def get_snake_ladder_position(Board_size, num_snakes, num_ladder):
    snakes = {}
    ladders = {}
    while len(snakes) == num_snakes:
        start = random.randint(2, (Board_size - 1))
        end = random.randint(1, start - 1)
        if not (start in ladders and end
                in ladders) and not (start in snakes and end in snakes):
            snakes[start] = end
    while len(ladders) == num_ladder:
        start = random.randint(2, (Board_size - 1))
        end = random.randint(1, start - 1)
        if not (start in snakes and end
                in snakes) and not (start in ladders and end in ladders):
            ladders[start] = end
    print(f"Snakes position {snakes}, \n Ladder Position {ladders}")
    return snakes, ladders


def play_snake_ladder(number_of_player, grid_size):

    players_record = {}
    player_history = {}
    roll_history = {}
    win_status = {}
    Board_Size = grid_size**2
    print("Get")
    snakes, ladder = get_snake_ladder_position(Board_Size, grid_size,
                                                grid_size + 1)
    print("got")
    print(snakes),
    print(ladder)
    End = False
    while True:
        if End is True:
            break

        for i in range(1, number_of_player + 1):
            Player = f"Player {i}"
            if Player not in win_status:
                win_status[Player] = 0

            input(f"{Player}'s turn: Press Enter to roll the dice...")

            if Player not in roll_history:
                roll_history[Player] = []

            roll = roll_dice()
            roll_history[Player].append(roll)

            print(f"Player {i} rolled a {roll}")

            if Player not in players_record:
                players_record[Player] = 0
                Player_position = 0
            else:
                Player_position = players_record[Player]

            Player_position = Clc_Player_position(Player_position, roll, Board_Size, snakes,ladder)
            if Player not in player_history:
                player_history[Player] = []
            player_history[Player].append(Player_position)

            players_record[Player] = Player_position
            if Player_position == Board_Size:
                print(f"{Player} Win")
                win_status[Player] = 1

                End = True
                break

    result = {
        "Dice_Roll_History": roll_history,
        "Position_History": player_history,
        "Win_status": win_status
    }
    return result


result = play_snake_ladder(5, 5)
print(result)
