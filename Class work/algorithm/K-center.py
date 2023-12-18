import numpy as np

def select_city(n, d, k):
    dist = [np.Infinity]*n
    centers = []
    farmost_city = np.random.randint(0,n)

    for i in range(k):
        centers.append(farmost_city)
        for j in range(n):
            dist[j] = min(dist[j], d[farmost_city][j])
        m = 0
        for j in range(n):
            if(dist[j] > dist[m]):
                m = j
        farmost_city = m
    
    return(centers)

def triangle_inequality(weights):
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(n):
                # Checking if triangle inequality is violated
                if weights[i][k] + weights[k][j] < weights[i][j]:
                    weights[i][j] = weights[i][k] + weights[k][j]
                    weights[j][i] = weights[i][j]  

    return weights

if __name__ == '__main__':
    nlist = [50, 100, 500, 1000, 2000] 
    klist = [10, 15, 20, 25]
    for n in nlist:
        d = np.zeros((n,n))
        for i in range(n):
            for j in range(i):
                if(i != j):
                    d[i,j] = d[j,i] = np.random.randint(1,20)
        d = triangle_inequality(d.copy())
        for k in klist:
            print('for', n, 'cities, selected ', k, ' centers are', select_city(n, d, k))