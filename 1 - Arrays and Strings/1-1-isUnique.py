# Time: O(n)
# Space: O(1)
def isUnique(s):
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

word = "Cracking The Coding Interview"
print(isUnique(word))