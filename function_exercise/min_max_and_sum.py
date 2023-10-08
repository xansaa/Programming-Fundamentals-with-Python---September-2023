def min_max_sum_number(some_number):
    input_num = []
    for num in some_number:
        input_num.append(int(num))
    input_num.sort()
    min_num = input_num[0]
    max_num = input_num[-1]
    sum_num = 0
    for num in input_num:
        sum_num += num
    return min_num, max_num, sum_num


number_as_string = input().split()
min_num, max_num, sum_num = min_max_sum_number(number_as_string)
print(f"The minimum number is {min_num}""\n"f"The maximum number is {max_num}""\n"f"The sum number is: {sum_num}")