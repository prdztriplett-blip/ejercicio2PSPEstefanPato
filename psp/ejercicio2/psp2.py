import math

class PSP2(object):
    def __init__(self, x, dof, num_seg=10):
        self.x = x
        self.dof = dof
        self.num_seg = num_seg
        self.w = x / num_seg
        
    def f(self,x):
        v = self.dof
        num = math.gamma((v+1)/2)
        den = math.sqrt(v*math.pi)*math.gamma(v/2)
        return (num/den)*(1+(x**2/v))**(-(v+1)/2)
    
    def calcular(self):
        a =0
        b=self.x
        h=self.w
        
        suma = self.f(a)+self.f(b)
        
        for i in range (1, self.num_seg):
            xi = a+i*h
            if i%2 ==0:
                suma += 2 * self.f(xi)
            else:
                suma += 4 * self.f(xi)
            
        integral = (h/3)*suma
        
        return integral