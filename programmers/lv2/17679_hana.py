def solution(m, n, board):
    answer = 0

    for row in range(m - 1):
        for col in range(n - 1):
            if board[row][col] == board[row + 1][col] and board[row][col] == board[row][col + 1] and board[row][col] == \
                    board[row + 1][col + 1]:
                answer += 4
                # pre = board[row][col]
            board[row][col] = ' '
            board[row + 1][col] = ' '
            board[row][col + 1] = ' '
            board[row + 1][col + 1] = ' '
            print(''.join(board))
    # for row_idx in range(n-1):
    #     for col_idx in range(m-1):
    #         target = board[row_idx][col_idx]
    #         # print("target: ", target)
    #         next_col = col_idx+1
    #         if target == board[next_row][col_idx] and target == board[row_idx][next_col] and target == board[next_row][next_col]:
    #             print("폭파!")
    # board[next_row][col_idx] = '' #오른쪽
    # board[row_idx][next_col] = '' #아래
    # board[next_row][next_col] = '' #대각선아래

    return answer


if __name__ == '__main__':
    solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
