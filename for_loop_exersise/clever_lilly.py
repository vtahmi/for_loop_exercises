# lily_age = int(input())
# washing_machine_price = float(input())
# toy_price = int(input())
# birthday_money = 0
# deduction_money = 0
# toy_count = 0
# for num in range(1, lily_age + 1):
#     if num % 2 == 0:
#         birthday_money = birthday_money + num * 5
#         birthday_money -= 1
#     else:
#         toy_count += 1
# toy_money = toy_count * toy_price
# total_money = birthday_money + toy_money
# if total_money >= washing_machine_price:
#     extra = total_money - washing_machine_price
#     print(f"Yes! {extra:.2f}")
# else:
#     short = washing_machine_price - total_money
#     print(f"No! {short:.2f}")

lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
birthday_money = 0
deduction_money = 0
for num in range(1, lily_age + 1):
    if num % 2 == 0:
        birthday_money = birthday_money + num * 5
        birthday_money -= 1
    else:
        birthday_money += toy_price
if birthday_money >= washing_machine_price:
    extra = birthday_money - washing_machine_price
    print(f"Yes! {extra:.2f}")
else:
    short = washing_machine_price - birthday_money
    print(f"No! {short:.2f}")





