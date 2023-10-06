def repeat_string(word, n):
    result = word * n
    return result


strings = input()
num_repeat = int(input())
result = repeat_string(strings, num_repeat)
print(result)
