num_snowballs = int(input())
weight_snowballs = 0
time_to_fly = 0
quality_balls = 0
total_value = 0

for current_snowballs in range(num_snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    snowballs_count = (current_weight / current_time) ** current_quality
    if snowballs_count > total_value:
        weight_snowballs = current_weight
        time_to_fly = current_time
        quality_balls = current_quality
        total_value = snowballs_count
print(f"{weight_snowballs} : {time_to_fly} = {int(total_value)} ({quality_balls})")