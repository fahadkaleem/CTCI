def palindromePermutation(word):
    # Time: O(n)
    if len(word)==0:
        return True
    countArray = [0 for i in range(127)]
    countOdds = 0
    for i in word:
        # if i == " ":
        #     continue
        asc = ord(i)
        countArray[asc]+=1
    for i in countArray:
        if countOdds >1:
            return False
        if i%2==1:
            countOdds+=1
    return True

print(palindromePermutation("tacocat"))
