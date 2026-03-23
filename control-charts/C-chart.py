# C chart without Revised C
import matplotlib.pyplot as plt
import math
y_axis=[3,5,4,8,9,7,10,13,12,15]
x = list(range(1, len(y_axis) + 1))
c_bar =  sum(y_axis)/len(y_axis)
print(f"c_bar = {c_bar}")
UCL = c_bar +  3 * math.sqrt(c_bar)
print(f"UCL  = {UCL:.1f}")
LCL = c_bar -  3 * math.sqrt(c_bar)
plt.plot(x,y_axis, marker='o', label='Data')
plt.axhline(y=c_bar, color='green', linestyle='--', label=f'c_bar = {c_bar:.1f}')
plt.axhline(y=UCL, color='red', linestyle='--', label=f'UCL = {UCL:.1f}')
if LCL < 0:
    print(f"LCL = 0")
    plt.axhline(y=0, color='blue', linestyle='--', label=f'LCL  = 0')
else:
    print(f"LCL = {LCL:.1f}") 
    plt.axhline(y=LCL, color='blue', linestyle='--', label=f'LCL  = {LCL:.0f}')       
if any(value > UCL for value in y_axis):
    print("The process is not in control.")
else:
    print("The process is in control.")    
plt.xlabel(input("Name the  x-axis: "))
plt.ylabel(input("Name the y-axis:"))
plt.axis('square')
plt.title('C chart')
plt.grid()
plt.legend()
plt.show()