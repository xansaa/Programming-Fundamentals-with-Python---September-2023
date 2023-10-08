def loading_bar(some_number):
    if some_number == 100:
        print("100% Complete!\n[%%%%%%%%%%]")
        return
    numbers = some_number // 10
    procent = 10 - numbers
    print(f"{some_number}% [{numbers * '%'}{procent * '.'}]\n""Still loading...")


input_number = int(input())
loading_bar(input_number)