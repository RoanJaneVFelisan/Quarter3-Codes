import numpy as np

names = ["Aston", "Marvoun", "Jane"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],  # Aston's steps
    [4000, 4100, 3900, 4200, 4600],  # Marvoun's steps
    [6000, 5800, 5900, 6100, 6200]   # Jane's steps
])

daily_totals = []

for day_index in range(len(days)):
    total = 0
    for person_index in range(len(names)):
        total += steps[person_index][day_index]
    daily_totals.append(total)

print("Total steps per day:")
for i in range(len(days)):
    print(days[i], ":", daily_totals[i])

max_index = daily_totals.index(max(daily_totals))
print("\nMost active day overall:")
print(days[max_index], ": ", daily_totals[max_index], "steps")
