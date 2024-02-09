# num_climbers_groups = int(input())
# musala = 0
# montblan = 0
# kilimanjaro = 0
# k2 = 0
# everest = 0
# for _ in range(num_climbers_groups):
#     num_climbers = int(input())
#     if num_climbers <= 5:
#         musala += num_climbers
#     elif num_climbers <= 12:
#         montblan += num_climbers
#     elif num_climbers <= 25:
#         kilimanjaro += num_climbers
#     elif num_climbers <= 40:
#         k2 += num_climbers
#     else:
#         everest += num_climbers
# total_climbers = musala + montblan + kilimanjaro + k2 + everest
# musala_percent = musala / total_climbers * 100
# montblan_percent = montblan / total_climbers * 100
# kilimanjaro_percent = kilimanjaro / total_climbers * 100
# k2_percent = k2 / total_climbers * 100
# everest_percent = everest / total_climbers * 100
# print(f"{musala_percent:.2f}%")
# print(f"{montblan_percent:.2f}%")
# print(f"{kilimanjaro_percent:.2f}%")
# print(f"{k2_percent:.2f}%")
# print(f"{everest_percent:.2f}%")


num_climbers_groups = int(input())
mussala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_climbers = 0
for _ in range(num_climbers_groups):
    num_climbers = int(input())
    total_climbers += num_climbers
    if num_climbers <= 5:
        mussala += num_climbers
    elif num_climbers <= 12:
        montblanc += num_climbers
    elif num_climbers <= 25:
        kilimanjaro += num_climbers
    elif num_climbers <= 40:
        k2 += num_climbers
    else:
        everest += num_climbers
mussala_percent = mussala / total_climbers * 100
montblanc_percent = montblanc / total_climbers * 100
kilimanjaro_percent = kilimanjaro / total_climbers * 100
k2_percent = k2 / total_climbers * 100
everest_percent = everest / total_climbers * 100
print(f"{mussala_percent:.2f}%")
print(f"{montblanc_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")




