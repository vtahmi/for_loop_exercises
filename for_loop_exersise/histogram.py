numbers_count = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(numbers_count):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number <= 399:
        p2 += 1
    elif number <= 599:
        p3 += 1
    elif number <= 799:
        p4 += 1
    else:
        p5 += 1
p1_percent = p1 / numbers_count * 100
p2_percent = p2 / numbers_count * 100
p3_percent = p3 / numbers_count * 100
p4_percent = p4 / numbers_count * 100
p5_percent = p5 / numbers_count * 100
print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")





















