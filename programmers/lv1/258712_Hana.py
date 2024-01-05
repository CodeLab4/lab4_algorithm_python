def solution(friends, gifts):
    answer = 0

    gift_level = dict.fromkeys(friends, 0)
    result_dic = dict.fromkeys(friends, 0)
    data = [[0] * len(friends) for _ in range(len(friends))]

    for row in gifts:
        sender, receiver = row.split(' ')
        data[friends.index(sender)][friends.index(receiver)] += 1

    for friend in friends:
        sent = sum(data[friends.index(friend)])
        received = sum(data[i][friends.index(friend)] for i in range(len(friends)))
        gift_level[friend] = sent - received

    for friend in friends:
        for other in friends:
            if friend != other:
                sender_gifts = data[friends.index(friend)][friends.index(other)]
                receiver_gifts = data[friends.index(other)][friends.index(friend)]
                if sender_gifts > receiver_gifts or (
                        sender_gifts == receiver_gifts and gift_level[friend] > gift_level[other]):
                    result_dic[friend] += 1

    answer = max(result_dic.values())

    return answer
