# np chart
import math
import matplotlib.pyplot as plt
np = [2,5,0,14,3,0,1,0,18,8,6,0,3,0,6]
tt = input("Enter total items : ")
sumation_n = tt * 15
print(f"∑n = {sumation_n}")
sumation_np = sum(np)
print(f"∑np = {sumation_np}")
p_bar = sumation_np/sumation_n
print(f"p_bar = {p_bar}")
np_bar = tt * p_bar 
print(f"np_bar = {np_bar:.4f}")
UCL = np_bar + 3 * math.sqrt((np_bar)*(1-p_bar))
print(f"UCL = {UCL:.4f}")
LCL = np_bar - 3 * math.sqrt((np_bar)*(1-p_bar))
x_axis = range(1,len(np)+1)
plt.xlim(0,len(np)+4)
plt.ylim(0,max(np)+4)
plt.plot(x_axis,np,marker ='o',label="Data")
plt.axhline(y=np_bar,color = 'r',linestyle ='--',label = f"np_bar = {np_bar:.4f}") 
plt.axhline(y=UCL,color = 'b',linestyle ='--',label = f"UCL = {UCL:.4f}") 
if LCL < 0:
    print("LCL = 0.")
    plt.axhline(y=0,color = 'g',linestyle ='--',label = f"LCL = 0")
else:    
    print(f"LCL = {LCL:.4f}")
    plt.axhline(y=LCL,color = 'g',linestyle ='--',label = f"LCL = {LCL:.4f}")
if any(value > UCL for value in np):
    print("The Process is in control.") 
else:
    print("The Process is in control. ")  
# plt.xlabel(input("Enter the name of x-axis: "))   
plt.xlabel('Date')
# plt.ylabel(input("Enter the name of y-axis: "))  
plt.ylabel('No.of Defectives (np)') 
plt.title('np-chart')             
plt.grid()
plt.legend()
plt.show()     