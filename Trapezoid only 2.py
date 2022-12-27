def Trapezoid(a,b,f):
    n = 100
    def trapezoid(f,a,b,n=100):
        h=(b-a)/n
        sum = 0.0
        for i in range (1,n):
            x = a+i*h
            sum = sum +f(x)
        integral = (h/2)*(f(a)+2*sum+f(b))
        return integral
    integral = trapezoid(f,a,b,n)
    print(a,",",b,",",round(integral,2))


for i in range(1,5):
    Trapezoid(i+2,i+4,lambda x: x**2 + 4)
    
for i in range(5,10):
    Trapezoid(i+1,i+3,lambda x: x**2 + 4)

for i in range(1,10):
    Trapezoid(i+10,i+12,lambda x: x**2 - 1)

for i in range(0,10):
    Trapezoid(i+1,i+2,lambda x: x**3 + 2*x**2 + 3)

for i in range(0,10):
    Trapezoid(i+5,i+12,lambda x: 6*x**2 + 10)

for i in range(1,10):
    Trapezoid(i+1,i+2,lambda x: x**3 + x**2)

for i in range(1,10):
    Trapezoid(i+2,i+3,lambda x: x**2 + x)

for i in range(1,5):
    Trapezoid(i+1,i+5,lambda x: x**4 + 2)

for i in range(0,10):
    Trapezoid(i+1,i+7,lambda x: 7*x**4 + 1)

for i in range(0,10):
    Trapezoid(i+1,i+4,lambda x: x**5)
