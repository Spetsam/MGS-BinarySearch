def naive_search(l, target): #I defined naive search for future usage
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low=None, high=None): #Binary search for future usage
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low:
        return -1
    midpoint = (low + high) // 2 #How many times 2 goes into length
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        return binary_search(l, target, midpoint + 1, high)
    
if __name__=='__main__':
    
    l = [1, 3 ,5, 10 ,12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))