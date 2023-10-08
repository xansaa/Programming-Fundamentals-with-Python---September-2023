def sort_number(some_number):
    input_num = []
    for num in some_number:
        input_num.append(int(num))
    input_num.sort()
    return input_num


number_as_string = input().split()
result = sort_number(number_as_string)
print(result)