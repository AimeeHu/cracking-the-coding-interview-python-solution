def reverse_str(string):
	return string[::-1]


#--------------------test-------------------
inputstr = "abcdefghijk"
if reverse_str(inputstr)=="kjihgfedcba":
	print "test passed"
else:
	print "failed"