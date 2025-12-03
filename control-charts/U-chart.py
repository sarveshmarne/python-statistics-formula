# U chart
import math
import matplotlib.pyplot as plt
n = [25,20,25,15,25,15,20,15,15,25,20,20,15,25,20,25,15,25,15,25]
c = [12,5,7,7,10,4,6,2,4,10,9,12,14,6,7,12,5,6,8,4]
u = [c_i/ n_i for n_i, c_i in zip(n , c)]
print(f"U = {u}")
u_bar  = sum(u)/len(n)
all_UCL_bar = [ u_bar + 3 * math.sqrt((u_bar)/(n_i)) for n_i in n]
print(f"column UCL_bar = {all_UCL_bar}")
all_LCL_bar = [ u_bar - 3 * math.sqrt((u_bar)/(n_i)) for n_i in n]
all_LCL_bar = [max(0,lcl)for lcl in all_LCL_bar]
print(f"column LCL_bar = {all_LCL_bar}")
print(f"u_bar (CL) = {u_bar:.4f}")
n_bar =  sum(n)/len(n)
print(f"n_bar = {n_bar:.4f}")
UCL = u_bar + 3 * math.sqrt((u_bar)/(n_bar))
print(f"UCL is = {UCL:.4f}")
LCL = u_bar - 3 * math.sqrt((u_bar)/(n_bar))
x_axis = range(1,len(n)+1)
plt.ylim(0, (max(u) + 0.2))
plt.xlim(0,len(n))
plt.plot(x_axis,u, marker="o",label="Data")
plt.axhline(y = u_bar, color = 'g', linestyle = '--',label = f"u_bar = {u_bar:.4f}")
plt.axhline(y = UCL, color = 'r',linestyle = '--',label =f"UCL = {UCL:.4f}" )    
if LCL < 0:
    print("LCL is = 0.")
    plt.axhline(y = 0, color = 'b',linestyle = '--',label =f"LCL = 0" )  
else:    
    print(f"LCL is = {LCL:.4f}")
    plt.axhline(y = LCL, color = 'b',linestyle = '--',label =f"LCL = {LCL:.4f}" )  
if any(value > UCL for value in u):
    print("The process is not in control.")
else:
    print("The process is in control.")
# plt.xlabel(input("Enter the name of x-axis: ")) 
plt.xlabel('No. of Carpet Inspected') 
# plt.ylabel(input("Enter the name of y-axis: "))   
plt.ylabel('No. of Defects')
plt.title('U chart')
# plt.axis('square')
plt.legend()
plt.grid()
plt.show()