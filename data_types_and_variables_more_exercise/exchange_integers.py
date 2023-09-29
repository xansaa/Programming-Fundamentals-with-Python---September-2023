a = int(input())
b = int(input())

print("Before: ")
print(f"a = {a}")
print(f"b = {b}")

before = a
a = b
b = before

print("After: ")
print(f"a = {a}")
print(f"b = {b}")


