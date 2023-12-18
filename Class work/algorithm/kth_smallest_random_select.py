import random
from timeit import default_timer as timer


def KthSmallest(X, n, k):
    start = timer()

    z, rc, compc = KthSmallestElement(X, 0, n - 1, k, 0, 0)

    end = timer()
    t =  (end - start)
    return(z, rc, compc, t)

def KthSmallestElement(X, l, r, k, rc, compc):

    if(l == r):
        compc += 1
        return X[l], rc, compc
     
    pos, compc = randomPartition(X, l, r, compc)
 
    compc += 1   
    if (pos - l == k - 1):
        return X[pos], rc , compc

    compc += 1
    if (pos - l > k - 1):
        rc += 1 
        return KthSmallestElement(X, l, pos - 1, k, rc, compc)
    rc += 1 
    return KthSmallestElement(X, pos + 1, r,k - pos + l - 1, rc, compc)



def partition(X, l, r, compc):
    x = X[r]
    i = l
    for j in range(l, r):
        compc += 1
        if (X[j] <= x):
            X[i], X[j] = X[j], X[i]
            i += 1
    X[i], X[r] = X[r], X[i]
    return i, compc


def randomPartition(X, l, r, compc):
    
    n = r - l + 1
    key = int(random.random() * n)
    X[l+key], X[r] = X[r], X[l+key]
    return partition(X, l, r, compc)


if __name__ == '__main__':
    X = [12, 3, 5, 7, 4, 19, 26]
    k = 3
    print("K'th smallest element is", KthSmallest(X, len(X), k))
 