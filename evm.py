import os
from time import sleep
lin=[]
lip=[]
lis=[]
liv=[]
def cd():
	for i in range(n):
		print("\nEnter",i+1,"candidate details:")
		nm=input("Enter name:")
		lin.append(nm)
		p=input("Enter party:")
		lip.append(p)
		s=input("Enter symbol:")
		lis.append(s)
		liv.append(0)	
	os.system('clear')
def vote():
	print("\tVOTING START.......\n")
	sleep(1)
	while(1):
		print("PARTY \t\t\t SYMBOL\n")
		for i in range(n):
			print(lip[i],"\t\t\t",lis[i])
		print("\npress 0 for stop the vote\n")
		v=input("Enter vote by symbol:")
		if(v=='0'):
			break;
		for i in range(n):
			if(v==lis[i]):
				liv[i]=liv[i]+1
		os.system('clear')
	os.system('clear')
def result():
	print("\tRESULT......")
	sleep(1)
	for i in range(n):
		print("Name:",lin[i])
		print("Party:",lip[i])
		print("Symbol:",lis[i])
		print("Vote:",liv[i])
		print("\n\n")
	re=max(liv)
	for i in range(n):
		if(liv[i]==re):
			index=i
			break;
	print(lin[index],"is winner 🏆🏆")
print("THIS WORK IS DONE BY ELECTION CIMMISSION\n")
n=int(input("Enter the number of candidate:"))
cd()
vote()
result()