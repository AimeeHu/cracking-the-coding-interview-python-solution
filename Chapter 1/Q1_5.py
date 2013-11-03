def strCompress(string):
    compressed = []
    lastchar = "" 
    charcount = 0
    for char in string:
        if char == lastchar:
            charcount += 1
        else:
            if lastchar != "":
                compressed.append(lastchar+str(charcount))
            lastchar = char
            charcount = 1
    compressed.append(lastchar+str(charcount)) #append the last character
    compressedStr = ''.join(compressed)  # join the list into a string
    if len(compressedStr)<len(string):
        return compressedStr
    else:
        return string
        


#-------------------------test-----------------------
inputStrs = ["abcdddefg", "aabbbcccaaffesttt", ""]
expectedOutputs = ["abcdddefg","a2b3c3a2f2e1s1t3", ""]

for i in range(0,len(inputStrs)):
    if strCompress(inputStrs[i])==expectedOutputs[i]:
        print "test "+ str(i+1) + " passed"
    else:
        print "test "+ str(i+1) + " failed"


