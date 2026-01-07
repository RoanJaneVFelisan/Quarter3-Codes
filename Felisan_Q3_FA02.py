import numpy as np

names = ["Aston", "Marvoun", "Jane"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],  # Aston's steps
    [4000, 4100, 3900, 4200, 4600],  # Marvoun's steps
    [6000, 5800, 5900, 6100, 6200]   # Jane's steps
])

print("Daily steps (Monday to Friday):")

for i in range(len(names)):
    print(names[i], ":", steps[i])
