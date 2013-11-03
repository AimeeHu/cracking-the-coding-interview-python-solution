def isSubstring(s1, s2):
	return s2 in s1

def isRotation(s1,s2):
	s1s1 = s1 + s1
	return isSubstring(s1s1, s2)



#-----------------test-------------
s1 = "keitjkdss"
s2 = "itj"
print isRotation(s1,s2)  # True

