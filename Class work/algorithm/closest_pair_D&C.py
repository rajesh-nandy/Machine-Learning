import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer


def distance(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)** .5

def closest_pair(x,y):
    P = []
    for i in range(len(x)):
        if(P.count((x[i], y[i])) == 0):
            P.append((x[i], y[i]))
    
    P = sorted(P, key=lambda x: x[1])

    return(sorted_closest_pair(P))


def sorted_closest_pair(P):
    
    if(len(P)<=3):
        if(len(P)== 2) :
            return (P[0], P[1])
        else:
            l = [distance(P[0],P[1]), distance(P[1], P[2]), distance(P[0], P[2])]
            md = l.index(min(l))
            return(P[0 + md], P[(1+md)%3])

    mid = len(P)//2
    midPoint = P[mid]
    q0, q1 = sorted_closest_pair(P[0:mid])
    r0, r1 = sorted_closest_pair(P[mid:])

    qd, rd = distance(q0, q1), distance(r0, r1)
    if(qd>rd):
        c0, c1 = r0, r1
    else:
        c0, c1 = q0, q1

    d = min(qd,rd)
    strip = []
    for i in range(len(P)):
        if(abs(P[i][0] - midPoint[0]) < d ):
            strip.append(P[i])
    
    if(len(strip)> 1):
        j0, j1, new_d = strip_closest(strip, d)
        if(new_d < d):
            c0, c1 = j0, j1
    return (c0, c1)
    


def strip_closest(P, d):
    P = sorted(P, key=lambda x: x[1])
    new_d = np.inf
    j0, j1 = P[0], P[0]
    for i in range(len(P)):
        for j in range(i+1, min(len(P)-1, i+7) + 1):
            new_d = distance(P[i], P[j])
            if(new_d < d):
                d = new_d
                j0, j1 = P[i], P[j]
    
    return j0, j1, d
            




"""x = [19,  9, 16, 17, 17,  9,  8, 19, 18, 19,  5,  4,  6,  5,  6, 15, 15,  3, 12, 10]
y = [13, 12, 12,  7,  8, 13, 18,  8, 12, 14,  2,  1, 19,  3, 14,  7,  8,  4,  1,  11]

a, b = closest_pair(x,y)
print(a,b)"""


n_list = [1000, 2000, 5000, 7000, 10000, 15000, 20000, 30000, 50000, 60000]
for n in n_list:
    x = np.random.randint(1,100000, size = (n))
    y = np.random.randint(1,100000, size = (n))
    start = timer()

    a, b = closest_pair(x,y)

    end = timer()
    t =  (end - start)
    
    print("For sample size = ", n," closest pair: ", a , b,"\n\t distance = ", distance(a,b), "\n\ttime taken: ", t, " seconds\n")
