import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

print("Fibonacci sequence")

Max = int(input("Max amount of numbers: "))

StartNum = 1
Nums = [StartNum]

for i in range(1, Max):
    next_num = Nums[i-1] + Nums[i-2]
    Nums.append(next_num)  
    print(i + 1, ": ", Nums[i])

# Create the line plot
sns.lineplot(x=range(1, Max + 1), y=Nums)
plt.xlabel("Sequence Position")
plt.ylabel("Modified Fibonacci Number")
plt.title("Modified Fibonacci Sequence")
plt.show()

print("done!")