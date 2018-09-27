###### this is the first .py file ###########

####### write your code here ##########

if __name__ == "__main__":

	# Take the inputs in m, n and s
	m=int(input())
	n=int(input())

	s=[[0 for j in range(n)] for i in range(m)]
	arr=[[0 for j in range(n)] for i in range(m)]
	for i in range(m): 
		s[i][:]=input()
	
	for i in range(m):
		for j in range(n):
			count=1
			if(s[i][j]=='S'):
				minimum=min(min((n-1-j),j),min((m-1-i),i))
				print(f"{minimum} {i} {j}")
				for k in range(1,minimum+1):
					print("k="+str(k))
					if(s[i+k][j]=='S' and s[i-k][j]=='S' and s[i][j+k]=='S' and s[i][j-k] == 'S'):
						count+=4
					else:
						break
				arr[i][j]=count
			else:
				arr[i][j]=0
	print(arr)
	print(max(map(max, arr)))
	maximum=0
	maximum2=0
	for i in range(m):
		for j in range(n):
			if(arr[i][j]>maximum):
				maximum2=maximum
				maximum=arr[i][j]
			elif(arr[i][j]>maximum2):
				maximum2=arr[i][j]
	print(f"{maximum} {maximum2}")
