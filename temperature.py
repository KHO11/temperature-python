import numpy as np

temperatures = np.array([12, 15, 14, 10, 18, 20, 16])

# Average
average_temp = temperatures.mean()

print("Weekly Temperatures:")
for i, temp in enumerate(temperatures, start=1):
    print(f"Day {i}: {temp}°C")

print(f"\nAverage Temperature: {average_temp:.2f}")

# Above average (no loop needed)
above_average = temperatures[temperatures > average_temp]
print("Temperatures Above Average:", above_average)

# Max and Min (built-in NumPy functions)
print("Maximum Temperature:", temperatures.max())
print("Minimum Temperature:", temperatures.min())
