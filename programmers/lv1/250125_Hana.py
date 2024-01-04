def solution(board, h, w):
    answer = 0

    bh = [0, 0, -1, 1]
    bw = [-1, 1, 0, 0]

    for i in range(4):
        bh_check = h + bh[i]
        bw_check = w + bw[i]
        if 0 <= bh_check < len(board) and 0 <= bw_check < len(board[0]):
            if board[h][w] == board[bh_check][bw_check]:
                answer += 1

    return answer
