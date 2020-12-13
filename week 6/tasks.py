import pandas as pd
import matplotlib.pyplot as plt
from random import randint
# Activity 1
'''plt.scatter([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
plt.show()'''

# Acivity 2
'''x = [randint(0, 8) for _ in range(0, 11)]
y = [randint(0, 8) for _ in range(0, 11)]

plt.scatter(x , y)
plt.show()'''

# Activity 3
def squared(x, s):
    return (x ** s)
def act3():
    w = int(input("Enter the power now: "))
    x = [ a for a in range(-500, 501)]
    y = [ squared(n, w) for n in x]
    plt.scatter(x, y)
    plt.show()

#act3()

# Activity 4
def act4():
    df = pd.read_csv("data.csv")
    # Calculate weight and height ratios
    whrs = []
    for i, row in df.iterrows():
        whrs.append(row["Weight"] / row["Height"])

    # Add weight-height ratio as a column.
    df["WHR"] = whrs

    # Output into another CSV file
    df.to_csv("whr-data.csv", index=False)

#act4()

def act5():
    coin_outcome = [randint(0, 1) for _ in range(0, 50001)]
    coin_bol = []
    for n in coin_outcome:
        if n == 0:
            coin_bol.append(False)
        else:
            coin_bol.append(True)





