# using python slice
def reverse_str(string):
    return string[::-1]

# recursive implementation
def reverse_str_rec(s):
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    elif len(s) == 2:
        return s[-1] + s[0]
    else:
        return s[-1] + reverse_str_rec(s[1:-1]) + s[0]


#--------------------test-------------------
inputstr = "abcdefghijk"
if reverse_str(inputstr)==reverse_str_rec(inputstr)=="kjihgfedcba":
    print "test passed"
else:
    print "failed"