numbers = input().split(", ")
num_beggars = int(input())

beggars = [0] * num_beggars

for i in range(len(numbers)):
    beggars_index = i % num_beggars
    num = int(numbers[i])
    beggars[beggars_index] += num
print(beggars)

