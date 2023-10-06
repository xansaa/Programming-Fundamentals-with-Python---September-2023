number_as_string = input().split()
numbers = []

for num in number_as_string:
    numbers.append(abs(float(num)))

print(numbers)

