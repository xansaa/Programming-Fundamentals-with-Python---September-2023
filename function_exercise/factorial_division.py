def factorial(some_number):
    for digit in range(1, some_number):
        some_number *= digit
    return some_number


first_number = int(input())
second_number = int(input())
first_number_factorial = factorial(first_number)
second_number_factorial = factorial(second_number)
result = first_number_factorial / second_number_factorial
print(f"{result:.2f}")