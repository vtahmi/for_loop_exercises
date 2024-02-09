actor_name = input()
academy_points = float(input())
number_judges = int(input())
total_points = 0 + academy_points

for num in range(number_judges):
    judge_name = input()
    judge_points = float(input())
    judge_total_points = len(judge_name) * judge_points / 2
    total_points += judge_total_points
    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    short = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {short:.1f} more!")





