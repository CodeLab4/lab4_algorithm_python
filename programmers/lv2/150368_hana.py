import itertools


def solution(users, emoticons):
    # 1. 가입자 최대한 늘리기
    # 2. 판매액 최대한 늘리기

    # 행사 방식
    # n명의 사용자에게 이모티콘 m개를 할인해 판매
    # 할인율은 이모티콘마다 다를 수 있고, 10,20,30,40% 중 하나로 선택

    # 사용자 기준
    # 각 사용자는 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘 모두 구매
    # 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상 -> 이모티콘 구매 취소, 플러스 가입

    rate = [0.1, 0.2, 0.3, 0.4]

    combinations = itertools.product(rate, emoticons)
    for comb in combinations:
        price = comb[1] - (comb[1] * comb[0])

    answer = []

    return answer