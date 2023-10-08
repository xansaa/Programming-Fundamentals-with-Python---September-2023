def palindrome(some_number: str):
        if some_number == some_number[::-1]:
            return True
        return False


number_of_string = input().split(", ")
for number in number_of_string:
    print(palindrome(number))