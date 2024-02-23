#lesson 14 funcrion
def f(x):
    y = 2*x + 1
    return y
print("i will calculate f(2):")
print(f(2))

#qudratic exmple 2
def f(x):
    y = x**2 + 4*x + 1
    return y
print("f(1) is ", f(1))
#example 3
#make 2 function
#f(x) = 2x + 1
#g(x) = 1/x
#h(x) = x2

def f(x):
    y = 2*x + 1
    return y


def g(x):
    u = 1 / x
    return u
def h(s):
    r = s*2
    return r

print( h (g(f(1))))

# example 4
# more than one varirbaln

def distance(x1 , y1 , x2, y2):
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return d
print("the distance between (1,2) and (3,4) is " ,distance(1,2,3,4))

#make a function that calculates the average of 3 numbers for exampel the averge of 5,7,9 =(5+7+9)/3 = 7

def average(x,y,z):
    a = (x+y+z)/3
    return a
print(average(5,7,9))

#example 6
def sayhello():
    print("hello")
#used it 3 times
sayhello()
sayhello()
sayhello()

quit()