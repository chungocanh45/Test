import math

global_var = 9
x, y, z = 8, 3, 6

def max1():
    nmax = max(x, max(y, z))
    print(nmax)
    def sum():
        global_var = nmax*2
        print(global_var)
    sum()

max1()

print("-        Lambda:")
f = lambda x, y, z: (x+y)/z if z!=0 else print("z = 0")
print(f(4,5,9))
print(f(4,5,0))

print("-Nhan doi voi lambda:")
nhandoi = lambda a: a*2
print(nhandoi(9))

x = 10
def index():
    y = 6
    print(y)
    print(x)
index()