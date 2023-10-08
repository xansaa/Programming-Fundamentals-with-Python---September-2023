def perfect_number(some_number):
    divisor = 0
    for num in range(1, some_number):
        if some_number % num == 0:
            divisor += num
        if some_number == divisor:
            return True
    return False


number = int(input())
result = perfect_number(number)
if result:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")