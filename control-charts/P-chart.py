# P chart 
# When Sample size is constant
import math
import matplotlib.pyplot as plt
b = [15,20,10,30,25] #200
a = int(input("Enter the Sample size: "))
p_bar = sum(b)/(a*len(b))
print(f"p_bar is = {p_bar:.4f}")
UCL = p_bar + 3 * math.sqrt(((p_bar * (1 - p_bar)) / ((a*len(b))/len(b))))
print(f"UCL is = {UCL:.4f}")
LCL = p_bar - 3 * math.sqrt(((p_bar * (1 - p_bar)) / ((a*len(b))/len(b))))
y_axis = [val / a for val in b] 
x_axis = range(1,len(b)+1)
plt.ylim(0, (max(y_axis) + 0.1))
plt.plot(x_axis,y_axis, marker="o",label="Data")
plt.axhline(y = p_bar,color = 'r',linestyle = '--',label=f'p_bar = {p_bar:.2f}')
plt.axhline(y = UCL,color = 'g',linestyle = '--',label=f'UCL = {UCL:.4f}')
if LCL < 0:
    print("LCL is = 0.")
    plt.axhline(y=0,color = 'b',linestyle = '--',label=f'LCL = 0')
else:    
    print(f"LCL is = {LCL:.4f}")
    plt.axhline(y=LCL,color = 'b',linestyle = '--',label=f'LCL = {LCL:.4f}')
print(f"Percentage Defective = {[val * 100 for val in y_axis]}")
print(f"Fraction Defective (p) = {y_axis}")
if any(value > UCL for value in y_axis):
    print("The process is not in control.")
else:
    print("The process is in control.")    
plt.xlabel(input("Enter the name of x-axis: ")) 
plt.ylabel(input("Enter the name of y-axis: "))
plt.title('P chart')
plt.grid()
plt.axis('square')
plt.legend()
plt.show()