import pandas as pd
import matplotlib.pyplot as plt
from random import randint
# Load CSV file
df = pd.read_csv("data.csv")

# Loop through and add up!
'''
total = 0
rows = 0 # Track my row count
for i, row in df.iterrows():

    total += row["Height"]
    rows += 1

print(total / rows)  #  Print

# Calculate weight and height ratios
whrs = []
for i, row in df.iterrows():
    whrs.append(row["Weight"] / row["Height"])

# Add weight-height ratio as a column.
df["WHR"] = whrs

# Output into another CSV file
df.to_csv("processed-output.csv", index=False)'''

# Generate 2 sets of 30 random numbers between 0 and 100
'''
x = [randint(0, 100) for _ in range(0, 30)]
y = [randint(0, 100) for _ in range(0, 30)]

# This actually doe the visualisation
plt.scatter(x, y)
plt.show()'''


'''x = df["Weight"]
y = df["Height"]


# Plot and show! This function "scatter()" produces a scatter graph.
plt.scatter(x, y)
plt.show()
'''
'''
x = range(0, 100)
y = [n**5 for n in x]

plt.plot(x, y)
plt.show()'''

#Roll 100 6-sided dice.
rolls = [randint(1, 6) for _ in range(1, 100)]

# Count the number of times each number was rolled
numbers = range(1, 7)
bars = [rolls.count(n) for n in numbers]

# Plot and show bar chart.
plt.bar(numbers, bars)
plt.show()