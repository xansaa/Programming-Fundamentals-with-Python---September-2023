def is_even(number):
    input_num = []
    for num in number:
        input_num.append(int(num))
    filter_result = filter(lambda x: x % 2 == 0, input_num)
    return list(filter_result)


number_as_string = input().split()
result = is_even(number_as_string)
print(result)
