def solution(board, moves):
    answer = 0

    transposed = [list(row) for row in zip(*board)]
    dolls = []
    basket = []
    for row in transposed:
        dolls.append(row)

    for move in moves:
        move -= 1
        for i, doll in enumerate(dolls[move]):
            if doll != 0:
                if basket and basket[-1] == doll:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(doll)
                dolls[move][i] = 0
                break

    return answer
