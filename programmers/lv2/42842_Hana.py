def solution(brown, yellow):
    answer = []

    total = brown + yellow
    divisors = []
    for i in range(1, total + 1):
        if total % i == 0:
            divisors.append(i)

    if len(divisors) == 3:
        answer = [divisors[1] for _ in range(2)]

    else:
        for i in range(len(divisors)):
            for j in range(i, len(divisors)):
                if divisors[i] * divisors[j] == total and (divisors[i] - 2) * (divisors[j] - 2) == yellow:
                    answer.append(divisors[j])
                    answer.append(divisors[i])

    return answer
