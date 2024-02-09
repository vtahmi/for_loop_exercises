# for i in range(1, 101):
#     print(i)
# n = int(input())
# for i in range(1, n + 1, 3):
#     print(i)
# n = int(input())
# for i in range(n + 1):
#     if i % 2 == 0:
#         num = 2 ** i
#         print(num)
# n = int(input())
# for i in range(n, 0, -1):
#     print(i)
# text = input()
# for letter in text:
#     print(letter)
# text = input()
# for letter in range(len(text)):
#     print(text[letter])


# text = input()
# total = 0
# for letter in text:
#     if letter == "a":
#         total += 1
#     elif letter == "e":
#         total += 2
#     elif letter == "i":
#         total += 3
#     elif letter == "o":
#         total += 4
#     elif letter == "u":
#         total += 5
# print(total)

# number = int(input())
# total = 0
# for _ in range(number):
#     num = int(input())
#     total += num
# print(total)

# number = int(input())
# largest_num = - sys.maxsize
# smallest_num = sys.maxsize
# for _ in range(number):
#     num = int(input())
#     if num > largest_num:
#         largest_num = num
#     if num < smallest_num:
#         smallest_num = num
# print(f"Max number: {largest_num}")
# print(f"Min number: {smallest_num}")
#

# number_rows = int(input())
# left_sum = 0
# right_sum = 0
# for i in range(number_rows):
#     number = int(input())
#     left_sum += number
# for i in range(number_rows):
#     number = int(input())
#     right_sum += number
# if left_sum == right_sum:
#     print(f"Yes, sum = {left_sum}")
# else:
#     diff = abs(left_sum - right_sum)
#     print(f"No, diff = {diff}")

# number_rows = int(input())
# left_sum = 0
# right_sum = 0
# for i in range(2 * number_rows):
#     number = int(input())
#     if i < number_rows:
#         left_sum += number
#     else:
#         right_sum += number
# if left_sum == right_sum:
#     print(f"Yes, sum = {left_sum}")
# else:
#     diff = abs(left_sum - right_sum)
#     print(f"No, diff = {diff}")


# number_rows = int(input())
# even_num_sum = 0
# odd_num_sum = 0
# for i in range(number_rows):
#     number = int(input())
#     if i % 2 == 0:
#         even_num_sum += number
#     else:
#         odd_num_sum += number
# if even_num_sum == odd_num_sum:
#     print(f"Yes\nSum = {even_num_sum}")
# else:
#     diff = abs(even_num_sum - odd_num_sum)
#     print(f"No\nDiff = {diff}")

# for number in range(7, 1001, 10):
#     print(number)

# for number in range(1001):
#     if number % 10 == 7:
#         print(number)


# import sys
# numbers_count = int(input())
# largest_number = -sys.maxsize
# total = 0
# for i in range(numbers_count):
#     number = int(input())
#     if number > largest_number:
#         largest_number = number
#     if number <= largest_number:
#         total += number
# diff = abs(total - largest_number)
# calc = abs(largest_number - diff)
# if largest_number == diff:
#     print(f"Yes\nSum = {diff}")
# else:
#     print(f"No\nDiff = {calc}")

# numbers_count = int(input())
# p1 = 0
# p2 = 0
# p3 = 0
# p4 = 0
# p5 = 0
# for i in range(numbers_count):
#     number = int(input())
#     if number < 200:
#         p1 += 1
#     elif number <= 399:
#         p2 += 1
#     elif number <= 599:
#         p3 += 1
#     elif number <= 799:
#         p4 += 1
#     else:
#         p5 += 1
# p1_percent = p1 / numbers_count * 100
# p2_percent = p2 / numbers_count * 100
# p3_percent = p3 / numbers_count * 100
# p4_percent = p4 / numbers_count * 100
# p5_percent = p5 / numbers_count * 100
# print(f"{p1_percent:.2f}%")
# print(f"{p2_percent:.2f}%")
# print(f"{p3_percent:.2f}%")
# print(f"{p4_percent:.2f}%")
# print(f"{p5_percent:.2f}%")
#

# lily_age = int(input())
# washing_machine_price = float(input())
# toy_price = int(input())
# money_saved = 0
# toy_count = 0
#
# for i in range(1, lily_age + 1):
#     if i % 2 == 0:
#         money_saved += i * 5 - 1
#     else:
#         toy_count += 1
# total_money = toy_count * toy_price + money_saved
# extra = total_money - washing_machine_price
# if total_money >= washing_machine_price:
#     print(f"Yes! {extra:.2f}")
# else:
#     short = washing_machine_price - total_money
#     print(f"No! {short:.2f}")

# count_tabs = int(input())
# salary = int(input())
# total = 0
#
# for _ in range(count_tabs):
#     website_name = input()
#     if website_name == "Facebook":
#         total += 150
#     elif website_name == "Instagram":
#         total += 100
#     elif website_name == "Reddit":
#         total += 50
#     if salary <= total:
#         print(f"You have lost your salary.")
#         break
# else:
#     extra = abs(salary - total)
#     print(f"{extra}")


# count_tabs = int(input())
# salary = int(input())
#
# for _ in range(count_tabs):
#     website_name = input()
#     if website_name == "Facebook":
#         salary -= 150
#     elif website_name == "Instagram":
#         salary -= 100
#     elif website_name == "Reddit":
#         salary -= 50
#     if salary <= 0:
#         print(f"You have lost your salary.")
#         break
# else:
#     print(salary)

# actor_name = input()
# academy_points = float(input())
# num_judges = int(input())
# total = 0 + academy_points
# for _ in range(num_judges):
#     judge_name = input()
#     judge_points = float(input())
#     total_sum = len(judge_name) * judge_points / 2
#     total += total_sum
#     if total > 1250.5:
#         print(f"Congratulations, {actor_name} got a nominee for leading role with {total:.1f}!")
#         break
# else:
#     short = 1250.5 - total
#     print(f"Sorry, {actor_name} you need {short:.1f} more!")

# climber_groups = int(input())
# mussala = 0
# montblanc = 0
# kilimanjaro = 0
# k2 = 0
# everest = 0
# total = 0
#
# for _ in range(climber_groups):
#     climbers_count = int(input())
#     total += climbers_count
#     if climbers_count <= 5:
#         mussala += climbers_count
#     elif climbers_count <= 12:
#         montblanc += climbers_count
#     elif climbers_count <= 25:
#         kilimanjaro += climbers_count
#     elif climbers_count <= 40:
#         k2 += climbers_count
#     else:
#         everest += climbers_count
#
# mussala_percent = mussala / total * 100
# montblanc_percent = montblanc / total * 100
# kilimanjaro_percent = kilimanjaro / total * 100
# k2_percent = k2 / total * 100
# everest_percent = everest / total * 100
# print(f"{mussala_percent:.2f}%")
# print(f"{montblanc_percent:.2f}%")
# print(f"{kilimanjaro_percent:.2f}%")
# print(f"{k2_percent:.2f}%")
# print(f"{everest_percent:.2f}%")
# import math
# 
# tournaments_count = int(input())
# starting_points = int(input())
# 
# w = 0
# total = 0 + starting_points
# for _ in range(tournaments_count):
#     reached_phase = input()
#     if reached_phase == "W":
#         w += 1
#         total += 2000
# 
#     elif reached_phase == "F":
#         total += 1200
#     elif reached_phase == "SF":
#         total += 720
# average_points = math.floor((total - starting_points) / tournaments_count)
# percent_win = w / tournaments_count * 100
# print(f"Final points: {total}")
# print(f"Average points: {average_points}")
# print(f"{percent_win:.2f}%")

# exam_hour = int(input())   #0 до 23
# exam_minute = int(input())  #0 до 59
# arrival_hour = int(input())  #0 до 23
# arrival_minute = int(input())  #0 до 59
# exam_time = exam_hour * 60 + exam_minute
# arrival_time = arrival_hour * 60 + arrival_minute
# diff = arrival_time - exam_time
# if diff > 0:
#     print("On time")
#     if 1 >= diff >= -30:
#         print("On time")
#         print(f"{abs(diff)} minutes before the start")
#     elif -30 > diff > -60:
#         print("Early")
#         print(f"{abs(diff)} minutes before the start")
#     else:
#         hours = abs(diff // 60)
#         minutes = abs(diff % 60)
#         print(f"{hours}:{minutes:02d} hours before the start")
# elif diff >= 1:
#     print("Late")
#     if diff <= 59:
#         print(f"{diff} minutes after the start")
#     else:
#         hours = abs(diff // 60)
#         minutes = abs(diff % 60)
#         print(f"{hours}:{minutes:02d} hours after the start")
#
#

# exam_hour = int(input())
# exam_minute = int(input())
# arrival_hour = int(input())
# arrival_minute = int(input())
# exam_time = exam_hour * 60 + exam_minute
# arrival_time = arrival_hour * 60 + arrival_minute
# difference = arrival_time - exam_time
# if difference > 0:
#     print("Late")
#     if difference < 60:
#         print(f"{difference} minutes after the start")
#     else:
#         hh = difference // 60
#         mm = difference % 60
#         print(f"{hh}:{mm:02d} hours after the start")
# elif difference >= -30:
#     print("On time")
#     if difference != 0:
#         print(f"{abs(difference)} minutes before the start")
# else:
#     print("Early")
#     if difference > -60:
#         print(f"{abs(difference)} minutes before the start")
#     else:
#         hh = abs(difference) // 60
#         mm = abs(difference) % 60
#         print(f"{hh}:{mm:02d} hours before the start")



# exam_hour = int(input())
# exam_minute = int(input())
# arrival_hour = int(input())
# arrival_minute = int(input())
# exam_time = exam_hour * 60 + exam_minute
# arrival_time = arrival_hour * 60 + arrival_minute
# difference = arrival_time - exam_time
# if difference > 0:
#     print("Late")
#     if 1 <= difference < 60:
#         print(f"{difference} minutes after the start")
#     elif difference >= 60:
#         hh = difference // 60
#         mm = difference % 60
#         print(f"{hh}:{mm:02d} hours after the start")
# elif difference >= -30:
#     print("On time")
#     if difference != 0:
#         print(f"{abs(difference)} minutes before the start")
# if difference > -60:
#     print("Early")
#     print(f"{abs(difference)} minutes before the start")
#
# else:
#     print("Early")
#     hh = abs(difference) // 60
#     mm = abs(difference) % 60
#     print(f"{hh}:{mm:02d} hours before the start")

print(28 % 3)
print(17 % 10)


















































