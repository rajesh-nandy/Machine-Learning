from timeit import default_timer as timer


def KthSmallest(X, n, k):
    start = timer()

    z, rc, compc = KthSmallestElement(X, 0, n - 1, k, 0, 0)

    end = timer()
    t =  (end - start)
    return(z, rc, compc, t)

def KthSmallestElement(X, low, high, k, rc,compc):
    p = high - low + 1
    if(p<5):
        X.sort()
        return X[k], rc, compc

    median_list = []
    r = p//5
    for i in range(r):
        median = insertionSort_median_find(X,low+i*5, low+(i+1)*5-1)
        median_list.append(median)
    if(p%5 != 0):
        median = insertionSort_median_find(X,low+r*5, high)
        median_list.append(median)
    rc= rc + 1
    mm, rc, compc = KthSmallestElement(median_list, 0, len(median_list)-1, len(median_list)//2, rc, compc)
    
    A_greater, A_equal, A_lesser, compc= partition(X, mm, compc)
    
    if(len(A_lesser) > k):
        rc = rc +1
        compc = compc + 1
        return KthSmallestElement(A_lesser, 0, len(A_lesser)-1, k, rc,compc)
    elif((len(A_lesser) + len(A_equal)) >= k):
        compc = compc + 1
        return mm , rc, compc
    else:
        compc = compc + 1
        rc = rc +1
        return KthSmallestElement(A_greater, 0, len(A_greater)-1, k - (len(A_lesser) + len(A_equal)), rc, compc)



def partition(X, mm, compc):
    A_greater, A_equal, A_lesser = [], [], []
    for i in X:
        
        if(i < mm):
            compc = compc +1
            A_lesser.append(i)
        elif(i>mm):
            compc = compc +1
            A_greater.append(i)
        else:
            A_equal.append(i)
    return A_greater, A_equal, A_lesser, compc


    


def insertionSort_median_find(q, low, high):
    if(low == high)  :
        return q[low]
    for i in range(low+1, high+1):
        
        key = q[i]  
        j = i-1
        while j >= low and key < q[j]:  
            q[j+1] = q[j]  
            j -= 1
        q[j+1] = key
    return(q[(low+high)//2])



if __name__ == '__main__':
    p = [81, 33, 17, 51, 57, 49,35,11, 25, 37,3, 155, 78, 30, 4 , 1 ]
    k = 4
    z, rc, compc, t = KthSmallest(p,len(p),k)
    print(z, rc, compc, t)

