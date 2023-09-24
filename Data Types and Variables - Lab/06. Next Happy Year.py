years = int(input())

while True:
    years += 1
    years_is_string = str(years)
    if len(years_is_string) == len(set(years_is_string)):
        break
print(years)