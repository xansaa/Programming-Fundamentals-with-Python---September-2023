lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet_total_price = lost_fight_count // 2
sword_total_price = lost_fight_count // 3
shield_total_price = lost_fight_count // (3 * 2)
armor_total_price = shield_total_price // 2
expenses = helmet_price * helmet_total_price + sword_price * sword_total_price + shield_price * shield_total_price\
           + armor_price * armor_total_price
print(f"Gladiator expenses: {expenses:.2f} aureus")