def stringCompression(word):
    # Time: O(n)
    letterCount = 1
    output = ''
    for i in range(len(word)-1):
        if word[i]==word[i+1]:
            letterCount+=1
        else:
            output+=word[i]+ str(letterCount)
            letterCount = 1
    output+=word[-1]+str(letterCount)
    return output

print(stringCompression("aaaabbbbccccddddddddd"))

