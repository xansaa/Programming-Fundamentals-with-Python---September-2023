word = input()
result = ([str for str in word if str.lower() not in ['a', 'o', 'u', 'e', 'i']])
print("".join(result))
