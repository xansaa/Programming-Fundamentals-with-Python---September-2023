num_line = int(input())
total_sum = 0

for characters in range(num_line):
    count_characters = input()
    total_sum += ord(count_characters)

print(f"The sum equals: {total_sum}")