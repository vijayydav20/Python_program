y=int(input("Enter year:"))
m=int(input("Enter month:"))
d=int(input("Enter date:"))
td=0
for i in range(1,y):
	if(i%4==0 and i%100!=0 or i%400==0):
		td=td+366
	else:
		td=td+365
for i in range(1,m):
		if(i==2):
			if(y%4==0 and y%100!=0 or                y%400==0):
				td=td+29
			else:
				td=td+28
		else:
			if(i==4 or i==6 or i==9 or i==11):
				td=td+30
			else:
				td=td+31
td=td+d
rem=td%7
if(rem==0):
			print("SUNDAY")
if(rem==1):
			print("MONDAY")			
if(rem==2):
			print("TUESDAY")
if(rem==3):
			print("WEDNESDAY")
if(rem==4):
			print("THURSDAY")			
if(rem==5):
			print("FRIDAY")						
if(rem==6):
			print("SATURDAY")							
			
		