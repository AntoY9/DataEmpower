import time
import matplotlib.pyplot as plt
import numpy as np

def wait(mil=None,sec=None, min=None, hr=None): time.sleep(sec if sec else min * 60 if min else hr * 3600 if hr else mil / 1000)

def isEven(Num): 
    if Num % 2 == 0: 
        return True
    else:
        return False

i = 0
j = 1
Nums = []
print ("Welcome to the unsolvable math problem")
mode = int(input("Your mode, 1: (stream) 2: (num) "))
if mode == 2:
 num = input("Your number: ")
if mode == 1:
   num = 1
num = int(num)

while True:
   if mode == 2: 
    if isEven(num) == False:
        num = (num * 3) + 1
        Nums.append(num)
    else:
        num = num/2
        Nums.append(num)
    print(i , ": " , num)
    i+=1
    wait(mil=1)
    if num == 1:
        break;
   if mode == 1:
    if isEven(num) == False:
        num = (num * 3) + 1
    else:
        num = num/2
    print(num)
    
    wait(mil=1)
    if num == 1:
        j+=1
        num = j
        print("_____________________")
        print(j , ": ")
        print("_____________________")
    

plt.figure(figsize=(10, 6))
plt.plot(range(len(Nums)), Nums, marker='o', linestyle='-', color='blue')
plt.xlabel("Iteration")
plt.ylabel("Number")
plt.title("Collatz Conjecture Visualization")
plt.grid(True)
plt.show()




