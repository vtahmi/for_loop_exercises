import sys

num_rows = int(input())
largest_num = -sys.maxsize
total_sum = 0
for num in range(num_rows):
    number = int(input())
    if number > largest_num:
        largest_num = number
    total_sum += number
if largest_num == total_sum - largest_num:
    print(f"Yes\nSum = {largest_num}")
else:
    print("No")
    sum_others = total_sum - largest_num
    diff = abs(sum_others - largest_num)
    print(f"Diff = {diff}")


