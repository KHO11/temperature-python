import numpy as np

temperatures = np.array([12, 15, 14, 10, 18, 20, 16])

# Basic stats
average_temp = temperatures.mean()
median_temp = np.median(temperatures)

print("Weekly Temperatures:")
for i, temp in enumerate(temperatures, start=1):
    print(f"Day {i}: {temp}°C")

print(f"\nAverage Temperature: {average_temp:.2f}")
print(f"Median Temperature: {median_temp}")

# Above & below average
above_average = temperatures[temperatures > average_temp]
below_average = temperatures[temperatures < average_temp]

print("Temperatures Above Average:", above_average)
print("Temperatures Below Average:", below_average)

# Max, Min, Range
max_temp = temperatures.max()
min_temp = temperatures.min()
temp_range = max_temp - min_temp

print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)
print("Temperature Range:", temp_range)

# Count days
print("Number of hot days (above avg):", len(above_average))
print("Number of cool days (below avg):", len(below_average))

# Simple trend (compare first and last day)
if temperatures[-1] > temperatures[0]:
    print("Trend: Getting warmer")
elif temperatures[-1] < temperatures[0]:
    print("Trend: Getting cooler")
else:
    print("Trend: No change")
