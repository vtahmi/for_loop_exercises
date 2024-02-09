# num_open_tabs = int(input())
# salary = int(input())
# total_penalty = 0
# for _ in range(1, num_open_tabs + 1):
#     website_name = input()
#     if website_name == "Facebook":
#         total_penalty += 150
#     elif website_name == "Instagram":
#         total_penalty += 100
#     elif website_name == "Reddit":
#         total_penalty += 50
#     if salary <= total_penalty:
#         print("You have lost your salary.")
#         break
# else:
#     extra = salary - total_penalty
#     print(extra)
#

num_open_tabs = int(input())
salary = int(input())
for _ in range(1, num_open_tabs + 1):
    website_name = input()
    if website_name == "Facebook":
        salary -= 150
    elif website_name == "Instagram":
        salary -= 100
    elif website_name == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(salary)


























