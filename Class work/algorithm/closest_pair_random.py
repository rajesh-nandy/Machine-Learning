import random
import numpy as np
import math

class dict:
    def __init__(self,P, maxX, maxY):
        self.dictionary = []
        self.maxX = maxX
        self.maxY = maxY
        self.x = 0
        self.y = 0
        self.P = P
        self.a = None
        self.b = None
        self.d = np.infty
    
    def Make_dictionary(self):
        print("dict making")
        dist = self.d/2
        self.x, self.y= math.ceil(self.maxX/dist), math.ceil(self.maxY/dist)
        cols = [None]*self.y
        for i in range(self.x):
            self.dictionary.append(cols.copy())
        

    def Insert(self, point, i, j):
        print("add")
        if(self.dictionary[i][j]== None): self.dictionary[i][j] = []
        self.dictionary[i][j].append(point)
        
    def randomized_closest_pair(self):
        self.a, self.b = random.sample(self.P, 2)
        flag = self.closest_pair()
        while(flag == 1):
            self.dictionary.clear()
            flag = self.closest_pair()
        return self.a,self.b

        

    def distance(self, a, b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2)** .5


    def closest_pair(self):
        flag = 0
        self.d = self.distance(self.a, self.b)
        self.Make_dictionary()
        for p in self.P:
            m = math.floor(p[0] / (self.d/2))
            n = math.floor(p[1] / (self.d/2))
            print(self.a, self.b, self.d, self.x, self.y, p,m,n, end= " $ ")
            print(max(m-2,0),min(m+3, self.x), max(n-2,0), min(n+3, self.y), end= " $ ")
            
            closer_points = []
            for i in range(max(m-2,0),min(m+3, self.x)):
                for j in range(max(n-2,0), min(n+3, self.y)):
                    print(i, j)
                    if(self.dictionary[i][j] != None):
                        for k in self.dictionary[i][j]:
                            if(k!=p):
                                new_d = self.distance(p, k)
                                closer_points.append([k, new_d])
        
            closer_points = sorted(closer_points, key=lambda x: x[1])
            print(closer_points)
            
            if(closer_points != [] and closer_points[0][1]<self.d):
                self.d = closer_points[0][1]
                self.a, self.b = p, k
                flag = 1
                break
            else:
                self.Insert(p, m, n)
                print(self.dictionary)
                
        
        return flag
                        


    




if __name__ == "__main__":
    """n_list = [1000, 2000, 5000, 7000, 10000, 15000, 20000, 30000, 50000, 60000]

    for n in n_list:
        x = np.random.randint(1,100000, size = (n))
        y = np.random.randint(1,100000, size = (n))
        a, b = closest_pair(x,y)"""

    x = [19, 9, 16, 17, 17,  9,  8, 19, 18, 19,  5,  4,  6,  5,  6, 15, 15,  3, 12, 10]
    y = [13, 12, 12,  7,  8, 13, 18,  8, 12, 14,  2,  1, 19,  3, 14,  7,  8,  4,  1,  11]
    P = []
    for i in range(len(x)):
        if(P.count((x[i], y[i])) == 0):
            P.append((x[i], y[i]))
    
    
    grid = dict(P, max(x), max(y))
    a,b = grid.randomized_closest_pair()
    print(a,b)