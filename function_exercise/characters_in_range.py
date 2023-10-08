def all_characters(first_char,second_char):
    final_char = []
    for char in range(ord(first_char) + 1, ord(second_char)):
        final_char.append(chr(char))
    return final_char


first_characters = input()
second_characters = input()
final_result = all_characters(first_characters, second_characters)
print(" ".join(final_result))

