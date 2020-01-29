import numpy as np
from scipy.optimize import minimize

BOd = float(input("enter back odds..."))
LOd = float(input("enter lay odds..."))
BStk = float(input("enter back stake..."))
FB = float(input("free bet? (1/0)..."))

LCom = 0.02

def my_func(x, BOd, LOd, BStk, FB, LCom):
    Bwin = ((BOd-1) * BStk - x * (LOd - 1))
    Blose = (BStk * (FB - 1) + x * (1 - LCom))
    return (Bwin - Blose)**2

z = minimize(my_func, args=(BOd, LOd, BStk, FB, LCom), x0=1, method='nelder-mead')

x=z.x

if my_func(x, BOd, LOd, BStk, FB, LCom)>0.1:
  print("!error in minimize function!")
  exit()

profit = (BStk*(FB-1)+x*(1-LCom))
print("Backers stake for lay bet = ", round(x[0],2))
print("profit = ", round(profit[0],2))