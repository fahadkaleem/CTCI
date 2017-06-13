def isUniqueCharArray(s):
    # Time: O(n)
    # Space: O(1)
    if len(s) == 0:
        return True
    if len(s) > 128:
        return False
    charArray = [False for i in range(128)]
    for i in s:
        asc = ord(i)
        if charArray[asc]:
            return False
        charArray[asc] = True
    return True


def isUniqueBruteForce(s):
    # Time: O(n2)
    # Space: O(1)
    if len(s) == 0:
        return True
    for i in range(len(s)):
        for j in range(len(s)):
            if i!=j and s[i]==s[j]:
                return False
    return True


def isUniqueSort(s):
    # Time: O(nlogn)
    if len(s)==0:
        return True
    newString = ''.join(sorted(s))
    for i in range(len(s)-1):
        if newString[i]==newString[i+1]:
            return False
    return True

word = "Cracking The Coding Interview"
print(isUniqueCharArray(word))
print(isUniqueBruteForce(word))
print(isUniqueSort(word))
