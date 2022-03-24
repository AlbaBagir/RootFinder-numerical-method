def fx(x):
        fx = (x**3)-(2*x**2)-(5*x)+6
        return fx

def m(x1,y1,x2,y2):
        slope = (y2-y1)/(x2-x1)
        return slope 

def linear(slope,x1,y1):
        y = 0
        left = y-y1
        x = (left/slope)+x1
        return x

def findRoot(x1,x2):  
    d = x2-x1
    e = 0.00000000001
    y1 = fx(x1)
    while(y1>=e):
            x2 = x1 + d
            y1 = fx(x1)
            y2 = fx(x2)
            grad = m(x1,y1,x2,y2)    
            x1 = linear(grad,x1,y1)
            d = x2-x1
            d = d-(d*0.1)
          
    return x1
    
    
print(findRoot(-1,5))        




   



