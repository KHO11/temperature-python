import numpy as np

# Temperature data for 7 days
temperatures = np.array([12, 15, 14, 10, 18, 20, 16])

# Calculate average using NumPy
average_temp = np.mean(temperatures)

print("Weekly Temperatures:")

# Loop through temperatures
for i in range(len(temperatures)):
    print("Day", i + 1, ":", temperatures[i], "°C")

print("\nAverage Temperature:", average_temp)

# Find temperatures above average using a loop
above_average = []

for temp in temperatures:
    if temp > average_temp:
        above_average.append(temp)

print("Temperatures Above Average:", above_average)

# Find max and min using a loop
max_temp = temperatures[0]
min_temp = temperatures[0]

for temp in temperatures:
    if temp > max_temp:
        max_temp = temp
    if temp < min_temp:
        min_temp = temp

print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)