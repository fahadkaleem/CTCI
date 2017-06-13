def checkPermutationSort(a,b):
    # Time: O(nlogn)
    if len(a) != len(b):
        return False
    if len(a) ==0 and len(b) ==0:
        return True
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
    for i in range(len(a)):
        if a[i]!=b[i]:
            return False
    return True

def checkPermutationCount(a,b):
    # Time: O(n)
    pass



print(checkPermutationSort("appa","papa"))