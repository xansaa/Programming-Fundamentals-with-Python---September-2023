def calculations(operator, num_1, num_2):
    result = 0
    if operator == "multiply":
        result = num_1 * num_2
    elif operator == "divide":
        result = num_1 // num_2
    elif operator == "add":
        result = num_1 + num_2
    elif operator == "subtract":
        result = num_1 - num_2
    return result


input_operator = input()
a = int(input())
b = int(input())
result = calculations(input_operator, a, b)
print(result)