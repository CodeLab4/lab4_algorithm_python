def solution(numbers, hand):
    answer = ''

    left_thumb = '*'
    right_thumb = '#'

    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    for number in numbers:
        if number in [1, 4, 7]:
            left_thumb = number
            answer += 'L'
        elif number in [3, 6, 9]:
            right_thumb = number
            answer += 'R'
        elif number in [2, 5, 8, 0]:
            left_distance = abs(keypad[left_thumb][0] - keypad[number][0]) \
                            + abs(keypad[left_thumb][1] - keypad[number][1])
            right_distance = abs(keypad[right_thumb][0] - keypad[number][0]) \
                             + abs(keypad[right_thumb][1] - keypad[number][1])

            if left_distance > right_distance:
                right_thumb = number
                answer += 'R'
            elif left_distance < right_distance:
                left_thumb = number
                answer += 'L'
            elif left_distance == right_distance:
                if hand == 'left':
                    left_thumb = number
                    answer += 'L'
                else:
                    right_thumb = number
                    answer += 'R'

    return answer
