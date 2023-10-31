group_size = int(input())
days = int(input())
coins = 0
for adventure_day in range(1, days + 1):
    if adventure_day % 10 == 0:
        group_size -= 2
    if adventure_day % 15 == 0:
        group_size += 5
    if adventure_day % 3 == 0:
        coins -= group_size * 3
    if adventure_day % 5 == 0:
        coins += group_size * 20
        if adventure_day % 3 == 0:
            coins -= group_size * 2
    coins += 50
    coins -= group_size * 2

total_coins = int(coins / group_size)
print(f"{group_size} companions received {total_coins} coins each.")