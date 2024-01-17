import sys


def solution(t):
    if t[-1] != '0':
        print(-1)

    else:
        time = int(t)
        answer = []
        buttons = [300, 60, 10]
        for button in buttons:
            answer.append(str(time // button))
            time %= button
        print(' '.join(answer))


if __name__ == '__main__':
    solution(t=sys.stdin.readline().rstrip())
