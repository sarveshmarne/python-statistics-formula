# P chart 
# When Sample size is constant
import math
import matplotlib.pyplot as plt
a = [224,287,180,250,294,203,277,249,120,165]
b = [10,12,13,15,9,12,11,12,13,12] 
p_bar = sum(b)/sum(a)
print(f"p_bar is = {p_bar:.4f}")
UCL = p_bar + 3 * math.sqrt(((p_bar * (1 - p_bar)) / ((sum(a))/len(a))))
print(f"UCL is = {UCL:.4f}")
LCL = p_bar - 3 * math.sqrt(((p_bar * (1 - p_bar)) / ((sum(a))/len(a))))
if LCL < 0:
    print("LCL is = 0.")
    plt.axhline(y=0,color = 'b',linestyle = '--',label=f'LCL = 0')
else:    
    print(f"LCL is = {LCL:.4f}")
    plt.axhline(y=LCL,color = 'b',linestyle = '--',label=f'LCL = {LCL:.4f}')
x_axis = range(1,len(a)+1)
fraction_defective = [b / a for a, b in zip(a, b)]
print(f"Fraction Defective =  {fraction_defective}")
percentage_defective = [val * 100 for val in fraction_defective]
print(f"Percentage Defective  = {percentage_defective}")
plt.plot(x_axis,fraction_defective, marker="o",label="Data")
plt.axhline(y = p_bar,color = 'r',linestyle = '--',label=f'p_bar = {p_bar:.2f}')
plt.axhline(y = UCL,color = 'g',linestyle = '--',label=f'UCL = {UCL:.4f}')
if any(value > UCL for value in fraction_defective):
    print("The process is not in control.")
else:
    print("The process is in control.")          
plt.ylim(0, (max(fraction_defective) + 0.1))
# plt.xlabel(input("Enter the name of x-axis: ")) 
plt.xlabel('Date')
# plt.ylabel(input("Enter the name of y-axis: "))
plt.ylabel("Fraction Defective")
plt.title('P chart')
plt.grid()
# plt.axis('square')
plt.legend()
plt.show()