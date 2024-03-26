"""
Find PI to the Nth Digit - 
    Enter a number and have the program generate PI up to that many decimal places.
    Keep a limit to how far the program will go.
Solution:
    - Use the Pi - Chudnovsky algorithm (formula)
    Link: https://www.craig-wood.com/nick/articles/pi-chudnovsky/
"""
import math 


def calA_K(k, a_prev):
    x = -24*((6*k-5)*(2*k-1)*(6*k-1))/((k**3)*(640320**3))
    return x*a_prev

def pi_chudnovsky(Nth):
    a_prev = 1
    # init variable
    a_curr = 1
    b = 0
    sum_a = a_prev
    sum_b = 0

   
    for i in range(1,Nth+1):
        a_prev, a_curr = a_curr, calA_K(i,a_prev)
        b = a_curr*i
        sum_a += a_curr
        sum_b += b
    
    pi = (426880*sqrt(10005,Nth))/(13591409*sum_a + 545140134*sum_b)
    return pi
    
        
