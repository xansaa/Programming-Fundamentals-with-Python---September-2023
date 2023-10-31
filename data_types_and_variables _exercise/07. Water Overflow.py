num_lines = int(input())
total_liters = 0
tank = 255

for liters in range(num_lines):
    current_liters = int(input())
    if tank - current_liters < 0:
        print(f"Insufficient capacity!")
        continue
    tank -= current_liters
    total_liters += current_liters

print(total_liters)