# suppose it is an ASCII string
def is_unique(string):
    if len(string) > 256:
        return False
    else:
        isExit = [False] * 256;
        for char in string:
            if isExit[ord(char)]:   #function ord() would get the ASCII value of the char      
                return False
            else:
                isExit[ord(char)]=True
        return True



#--------------------test-------------------]
test_true = "abcdefghijklmn"
test_false = "andkgeowa"

if is_unique(test_true):
    print "test 1 passed"
else:
    print "test 1 failed"

if not is_unique(test_false):
    print "test 2 passed"
else:
    print "test 2 failed"