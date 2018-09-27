###### this is the second .py file ###########

####### write your code here ##########

######## Function to check character in range of characters ####
import sys
def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

####### Function to rotate a list of char by y ###############
def rotate(l, y):
   if len(l) == 0:
      return l
   y = -y % len(l) 
   return l[y:] + l[:y]

####### Main program #########################################
if __name__ == "__main__":

	# Take the inputs in k1, k2, k3 and s
	k1=input()
	k2=input()
	k3=input()
	s=input()

	# Initailize 3 empty list for the 3 range of characters
	l1=[]
	l2=[]
	l3=[]

	# Initialize list for output string
	out=[]

	# Check the character belong to which range
	for c in s:
		if c in char_range('a','i'):
			l1+=c
		elif c in char_range('j','r'):
			l2+=c
		elif c in char_range('s','z') or '_':
			l3+=c
	# Rotate the elements of list by the value given in k
	l1=rotate(l1,int(k1))
	l2=rotate(l2,int(k2))
	l3=rotate(l3,int(k3))

	# Place the rotated elements in the out list
	for c in s:
		if c in char_range('a','i'):
			out.append(l1.pop(0))
		elif c in char_range('j','r'):
			out.append(l2.pop(0))
		elif c in char_range('s','z') or '_':
			out.append(l3.pop(0))

	#Print the out list by converting it to a string
	print(''.join(out))