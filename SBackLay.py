import numpy as np
from scipy.optimize import minimize

#prompts to enter details of bet
BOd = float(input("enter back odds..."))
LOd = float(input("enter lay odds..."))
BStk = float(input("enter back stake..."))
FB = float(input("free bet? (1/0)..."))

#Lay commission 
LCom = 0.02

#function to return squared difference between bet outcomes, no negatives 
#x = lay stake
def my_func(x, BOd, LOd, BStk, FB, LCom):
    #return if back bet wins
    Bwin = ((BOd-1) * BStk - x * (LOd - 1))
    #return if back bet loses
    Blose = (BStk * (FB - 1) + x * (1 - LCom))
    return (Bwin - Blose)**2

#minimize function changes x to find lowest value returned by my_func
z = minimize(my_func, args=(BOd, LOd, BStk, FB, LCom), x0=1, method='nelder-mead')

#extract the value of x from all data returned in z
x=z.x

#error handler for if minimize function doesn't converge sufficiently 
if my_func(x, BOd, LOd, BStk, FB, LCom)>0.1:
  print("!error in minimize function!")
  exit()

profit = (BStk*(FB-1)+x*(1-LCom))
print("Backers stake for lay bet = ", round(x[0],2))
print("profit = ", round(profit[0],2))
