## Common Features Across All Control Charts
Regardless of chart type (C, np, P, or U), every chart performs the following:

## All Charts Have These Features:
- Plot sample data points
- Calculate a center line (mean value)
- Calculate UCL (Upper Control Limit) and LCL (Lower Control Limit)
- Plot center line, UCL, and LCL using dashed lines
- Check whether any point exceeds UCL or goes below LCL
- Determine if the process is in control
- Display clean visual output with:
  - Title
  - Axis labels
  - Grid
  - Legend

## Unique Features of Each Chart

## C Chart — Without Revised Limits
**Unique To This Chart:**
Used when defect counts per inspection unit are measured
Sample size is constant and usually 1

**Calculates:**
c̄ = average number of defects
Control limits depend only on c̄
LCL is reset to 0 if negative

## np Chart — Number of Defectives (Constant Sample Size)
**Unique To This Chart:**
Uses number of defectives (np) per sample
Requires sample size (n) to be constant

**Calculates:**
p̄ = average fraction defective
np̄ = n × p̄
Control limits based on binomial distribution
Plots the actual np values
Asks user for sample size n

## P Chart — Fraction Defective (Constant Sample Size)
**Unique To This Chart:**

**Accepts:**
a = constant sample size
b = number of defectives per sample

**Calculates:**
p̄ = b/a
Fraction defective for each sample
Plots fraction defective (p) instead of counts

**Also prints:**
percentage defective
fraction defective values

**More values to practice.**
# b = [11,9,13,11,9,12,11,7,8,12,13,10,14,7,9] #200
# b = [5,7,3,6,4,9,8,6,5,7] #100
# b = [25,30,22,27,18,20,19,28,24,26] #1000
# b = [9,7,14,15,8,7,9,11,16,12,26,18,11,8,10,10,15,13,9,12] #200
# b = [0,0,2,3,0,8,1,0,1,5] #400

## U Chart — Variable Sample Size
**Unique To This Chart:**
Used when sample size varies

**Accepts:**
n = sample sizes
c = number of defects

**Calculates:**
u values = c/n
ū (average defects per unit)
UCL & LCL for each sample, each with different width

**Generates columns of:**
Per-sample UCL values
Per-sample LCL values
Also computes overall UCL & LCL using average sample size (n̄)
Ideal when inspection units are not equal across samples