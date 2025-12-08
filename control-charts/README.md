# b = [11,9,13,11,9,12,11,7,8,12,13,10,14,7,9] #200
# b = [5,7,3,6,4,9,8,6,5,7] #100
# b = [25,30,22,27,18,20,19,28,24,26] #1000
# b = [9,7,14,15,8,7,9,11,16,12,26,18,11,8,10,10,15,13,9,12] #200
# b = [0,0,2,3,0,8,1,0,1,5] #400

# C Chart — Without Revised Limits
What It Does:
Accepts defect counts (y-values) for each sample
Calculates:
c̄ (mean number of defects)
UCL and LCL using standard C-chart formulas
Plots the C-chart with all data points
Adds center line, upper limit, and lower limit
Checks whether the process is in control
Allows user to name x-axis and y-axis
# np Chart — Number of Defectives (Constant Sample Size)
What It Does:
Takes a list of np values (count of defectives per sample)
Asks user for sample size (n)
Calculates:
p̄ (average proportion defective)
np̄ (mean number of defectives)
UCL & LCL for the np-chart
Plots the np-chart with control limits
Flags any samples outside UCL or LCL
# P Chart — Fraction Defective (Constant Sample Size)
What It Does:
Accepts:
a = sample sizes (constant)
b = defectives in each sample
Computes:
p̄ (average fraction defective)
UCL & LCL
Fraction defective for every sample
Plots the P-chart with center line and limits

Determines if the process is in control

Displays fraction defective and percentage defective
