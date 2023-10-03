import boards

numbers = [1, 76, 38, 96, 62, 41, 27, 33, 4, 2, 94, 15, 89, 25, 66, 14, 30, 0, 71, 21, 48, 44, 87, 73, 60, 50, 77, 45, 29, 18, 5, 99, 65, 16, 93, 95, 37, 3, 52, 32, 46, 80, 98, 63, 92, 24, 35, 55, 12,
           81, 51, 17, 70, 78, 61, 91, 54, 8, 72, 40, 74, 68, 75, 67, 39, 64, 10, 53, 9, 31, 6, 7, 47, 42, 90, 20, 19, 36, 22, 43, 58, 28, 79, 86, 57, 49, 83, 84, 97, 11, 85, 26, 69, 23, 59, 82, 88, 34, 56, 13]
winners = []
last_board = []
final_number = []


def count_final_score():
    sum = 0
    for row in range(len(last_board[0])):
        for col in range(len(last_board[0])):
            if last_board[0][row][col] != "X":
                sum += last_board[0][row][col]

    return sum * final_number[0]


def check_for_bingo():
    for board_nr in range(len(boards.real_boards)):
        # Check for 5 X's in a row
        for row in boards.real_boards[board_nr]:
            if row == ["X", "X", "X", "X", "X"]:
                if board_nr not in winners:
                    winners.append(board_nr)

        # Check for 5 X's in a column
        for col in range(5):
            column = [boards.real_boards[board_nr][row][col]
                      for row in range(5)]
            if column == ["X", "X", "X", "X", "X"]:
                if board_nr not in winners:
                    winners.append(board_nr)


def play_bingo():
    i = 0
    while i < len(numbers):
        # Mark cells if it's a score
        for board_nr in range(len(boards.real_boards)):
            for row_nr in range(len(boards.real_boards[board_nr])):
                for nr in range(len(boards.real_boards[board_nr][row_nr])):
                    if boards.real_boards[board_nr][row_nr][nr] == numbers[i]:
                        boards.real_boards[board_nr][row_nr][nr] = "X"
        check_for_bingo()
        if len(winners) == len(boards.real_boards):
            last_board.append(boards.real_boards[winners[-1]])
            final_number.append(numbers[i])
            return
        i += 1


if __name__ == '__main__':
    play_bingo()
    print("The last board to win is board nr",
          winners[-1] + 1, "with a score of: ", count_final_score())
    print("The final number that was drawn was: ", final_number[0])
    print(last_board)
