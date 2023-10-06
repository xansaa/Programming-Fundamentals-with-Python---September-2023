def solve(grade):
    if 2 <= grades <= 2.99:
        print("Fail")
    elif 3 <= grades <= 3.49:
        print("Poor")
    elif 3.5 <= grades <= 4.49:
        print("Good")
    elif 4.50 <= grades <= 5.49:
        print("Very Good")
    elif 5.50 <= grades <= 6:
        print("Excellent")


grades = float(input())
solve(grades)
