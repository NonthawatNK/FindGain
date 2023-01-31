
filename = "out.csv"
f=open(filename,"r",encoding="utf-8")
X=f.readlines()
n = len(X)
for i in range(0,n):
	if((X[i].count('A')==1) and (X[i].count('H')==1) and (X[i].count('M')==1) ):
		print("0")
	if((X[i].count('B')==1) and (X[i].count('D')==1) and (X[i].count('1')==1)):
		print("1")
	if((X[i].count('A')==1) and (X[i].count('G')==1) and (X[i].count('E')==1) and (X[i].count('I')==1) and (X[i].count('L')==1) ):
		print("2")
	if((X[i].count('A')==1) and (X[i].count('G')==1) and (X[i].count('E')==1) and (X[i].count('J')==1) and (X[i].count('D')==1) ):
		print("3")
	if((X[i].count('B')==1) and (X[i].count('C')==1) ):
		print("4")
	if((X[i].count('A')==1) and (X[i].count('G')==1) and (X[i].count('F')==1) and (X[i].count('I')==1) ):
		print("5")
	if((X[i].count('A')==1) and (X[i].count('G')==1) and (X[i].count('F')==1) and (X[i].count('J')==1) ):
		print("6")
	if((X[i].count('A')==1) and (X[i].count('H')==1) and (X[i].count('N')==1) ):
		print("7")
	if((X[i].count('A')==1) and (X[i].count('G')==1) and (X[i].count('E')==1) and (X[i].count('I')==1) and (X[i].count('K')==1) ):
		print("8")
	if((X[i].count('A')==1) and (X[i].count('G')==1) and (X[i].count('E')==1) and (X[i].count('J')==1) and (X[i].count('C')==1) ):
		print("9")