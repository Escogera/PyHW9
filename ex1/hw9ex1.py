# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

import emoji

board = list(range(1, 10))

winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print("--------------------------")
    for i in range(3):
        print(" | ", board[0 + i * 3], " | ", board[1 + i * 3], " | ", board[2 + i * 3], " | ")
    print("--------------------------")


def take_input(player_symbol):
    while True:
        symbol = input(f"Куда поставить: {player_symbol}? ")
        if not (symbol in "123456789"):
            print("Такой позиции нет, повторите свой выбор.")
            continue
        symbol = int(symbol)
        if str(board[symbol - 1]) in emoji.emojize(":cross_mark:") and emoji.emojize(":yellow_circle:"):
            print("Эта клетка занята")
            continue
        board[symbol - 1] = player_symbol
        break


def check_winner():
    for each in winning_combinations:
        if (board[each[0]-1] == board[each[1]-1] == board[each[2]-1]):
            return board[each[1]-1]
    else:
        return False


def game():
    count = 0
    while True:
        draw_board()
        if count % 2 == 0:            
            take_input(emoji.emojize(":cross_mark:"))
        else:
            take_input(emoji.emojize(":yellow_circle:"))
        if count > 3:
            winner = check_winner()
            if winner:
                draw_board()
                print(f"{winner} выиграл! ")
                break
        count += 1
        if count > 8:
            draw_board()
            print("Игра закончена, ничья!")
            break

game()