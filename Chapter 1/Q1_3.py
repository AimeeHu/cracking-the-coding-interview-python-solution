def isPermutation(string1, string2):
    if len(string1) != len(string2):
        return False
    dic = {}
    for char in string1:
        dic[char] = dic.get(char, 0) + 1
    for char in string2:
        if dic.get(char,0) <= 0:
            return False
        else:
            dic[char] -= 1
    return True



#------------------test-----------------
string1 = "abcdefghaa"
string2 = "aaabcdefgh"
string3 = "dkescvvade"
string4 = ""

if isPermutation(string1, string2):
    print "test 1 passed"
if not isPermutation(string1, string3):
    print "test 2 passed"
if not isPermutation(string1, string4):
    print "test 3 passed"