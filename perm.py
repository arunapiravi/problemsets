def perm(s):
	if len(s) == 0:
		return ""
	if len(s) == 1:
		return s
	
	perms = []
	for index in xrange(len(s)):
		char = s[index]
		rem = s[:index] + s[index+1:]
		for item in perm(rem):
			perms.append(char+item)
	return perms

print perm("abc") 
