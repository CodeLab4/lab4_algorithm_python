import sys


def calculate_change(n):
    money = 1000 - n
    coins = [500, 100, 50, 10, 5, 1]
    change = 0

    for coin in coins:
        change += money // coin
        money %= coin
    print(change)


if __name__ == '__main__':
    calculate_change(n=int(sys.stdin.readline()))
