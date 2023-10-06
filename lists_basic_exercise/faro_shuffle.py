strings = input().split()
shuffle_num = int(input())

for i in range(shuffle_num):
    deck = []
    middle_of_deck = len(strings) // 2
    left_part = strings[0:middle_of_deck]
    right_part = strings[middle_of_deck:]
    for j in range(len(left_part)):
        deck.append(left_part[j])
        deck.append(right_part[j])
    strings = deck

print(strings)