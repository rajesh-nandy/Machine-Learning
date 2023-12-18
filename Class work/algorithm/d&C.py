X = [12,30, 10, 56,78]

def min_max(list1, l, r):
    if l == r:
        return [list1[l], list1[r]]

    elif l+1 == r:
        if list1[l]>list1[r]:
            return [list1[l], list1[r]]
        else:
            return [list1[r], list1[l]]

    else: 
        mid = l + (r-1)//2
    leftmaxmin = min_max(list1, l, mid)
    rightmaxmin = min_max(list1, mid+1, r)
    return [max(leftmaxmin[0], rightmaxmin[0]), min(leftmaxmin[1], rightmaxmin[1])]


r = min_max(X, 0, len(X)-1)
print("max = ",  r[0], "\tmin = ", r[1])
    