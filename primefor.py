number=int(input("Enter the number"))
for j in range(1,number) :
	f=0
	for i in range(2,j) :
		if j % i == 0 :
			f=1
	if f!=1 :
		print(j)


	
