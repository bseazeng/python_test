# -*- coding:utf8 -*-
def symbol_test():
    a = 2
    b = 3
    sum_ab = a+b
    print (sum_ab) #5
    
    c = b-a
    print (c) #1
    
    m = a*b  #6
    print (m)
    
    power=2**3 #2*2*2=8
    print (power)
    
    print (1/3) #0.3333333333333333
    print (2/2) #1.0    
    print (3//2) #1
    
    print (9%7) #2
    
    print (1<<2) #4
    print (2<<2) #8
    
    print (8>>2) #2
if "__main__" == __name__:
    symbol_test()