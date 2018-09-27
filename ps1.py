###### this is the first .py file ###########

####### write your code here ##########


############# Main Function ###################
import sys
if __name__ == "__main__":

	# Take the inputs in m, n
	m=int(input())
	n=int(input())

	if(n<2 or n>105 or m<2 or m>105):
		sys.exit("Error, out of range")
	# Initialize s and arr of size m*n
	s=[[0 for j in range(n)] for i in range(m)]
	arr=[[0 for j in range(n)] for i in range(m)]

	# Read the input characters in s
	for i in range(m): 
		s[i][:]=input()
	
	# For each element in s, check if it forms a cross
	for i in range(m):
		for j in range(n):
			count=1
			if(s[i][j]=='S'):
				minimum=min(min((n-1-j),j),min((m-1-i),i))
				for k in range(1,minimum+1):
					if(s[i+k][j]=='S' and s[i-k][j]=='S' and s[i][j+k]=='S' and s[i][j-k] == 'S'):
						count+=4
					else:
						break
				arr[i][j]=count  # Store the length of cross in the array arr
			else:
				arr[i][j]=0  # if the element is dull the size of cross is 0
	# Initialize two numbers for maximum and 2nd maximum
	maximum=0
	maximum2=0

	# Find the maximum and second maximum
	for i in range(m):
		for j in range(n):
			if(arr[i][j]>maximum):
				maximum2=maximum
				maximum=arr[i][j]
			elif(arr[i][j]>maximum2):
				maximum2=arr[i][j]

	# Print the maximum and second maximum
	print(f"{maximum} {maximum2}")
