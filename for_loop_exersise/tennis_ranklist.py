import math

numb_competitions = int(input())
starting_points = int(input())
total_points = 0
won_competitions = 0
for _ in range(numb_competitions):
    win_runner_up = input()
    if win_runner_up == "W":
        total_points += 2000
        won_competitions += 1
    elif win_runner_up == "F":
        total_points += 1200
    elif win_runner_up == "SF":
        total_points += 720
final_points = total_points + starting_points
average_points = math.floor(total_points / numb_competitions)
percent_won = won_competitions / numb_competitions * 100
print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percent_won:.2f}%")
