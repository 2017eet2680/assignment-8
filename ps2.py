###### this is the second .py file ###########

####### write your code here ##########

def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)
def rotate(l, n):
	try:
		return l[n:] + l[:n]
	except:
		return

if __name__ == "__main__":
	k1=input()
	k2=input()
	k3=input()
	s=input()
	l1=[]
	l2=[]
	l3=[]
	out=[]
	for c in s:
		if c in char_range('a','i'):
			l1.append(c)
		if c in char_range('j','r'):
			l2.append(c)
		if c in (char_range('s','z') or '_'):
			l3.append(c)
	rotate(l1,k1)
	rotate(l2,k2)
	rotate(l3,k3)
	for c in s:
		if c in char_range('a','i'):
			out.append(l1.pop(0))
		if c in char_range('j','r'):
			out.append(l2.pop(0))
		if c in (char_range('s','z') or '_'):
			out.append(l3.pop(0))
	print(out)
