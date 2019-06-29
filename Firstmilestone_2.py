def blankline():
	print('\t\t\t|\t\t\t|')
def underline():
	print('\t  ---\t\t'*3)
def validate(Xs,Ys):
	winner=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(9,6,3),(7,5,3),(1,5,9)]#total winning sequence
	for (a,b,c) in winner:# searching the winning sequence on the board
		if a in Xs and b in Xs and c in Xs:

			print("*"*100,"\n"*3,"X wins\t"*3)
			exit()
		elif a in Ys and b in Ys and c in Ys:
			print("*"*100,"\n"*3,"Y wins\t"*3)
			exit()
		
def print_board(Xs,Ys):
	for i in range(11):
		if i in [0,2,4,6,8,10]:
			blankline()
		elif i in [3,7]:
			underline()
#
# first row
#
		elif i == 1:
			if 7 in Xs:
				print ('\t   X\t\t|',end="")
			elif 7 in Ys:
				print ('\t   Y\t\t|',end="")
			else:
				print ('\t\t\t|',end="")
			if 8 in Xs:
				print ('\t   X\t\t|',end="")
			elif 8 in Ys:
				print ('\t   Y\t\t|',end="")
			else:
				print ('\t\t\t|',end="")
			if 9 in Xs:
				print ('\t   X\t\t')
			elif 9 in Ys:
				print ('\t   Y\t\t')
			else:
				print ('\t\t\t')
#
# second row
#
		elif i == 5:
			if 4 in Xs:
				print ('\t   X\t\t|',end="")
			elif 4 in Ys:
				print ('\t   Y\t\t|',end="")
			else:
				print ('\t\t\t|',end="")
			if 5 in Xs:
				print ('\t   X\t\t|',end="")
			elif 5 in Ys:
				print ('\t   Y\t\t|',end="")
			else:
				print ('\t\t\t|',end="")
			if 6 in Xs:
				print ('\t   X\t\t')
			elif 6 in Ys:
				print ('\t   Y\t\t')
			else:
				print ('\t\t\t')
#
# Third row
#
		elif i == 9:
			if 1 in Xs:
				print ('\t   X\t\t|',end="")
			elif 1 in Ys:
				print ('\t   Y\t\t|',end="")
			else:
				print ('\t\t\t|',end="")
			if 2 in Xs:
				print ('\t   X\t\t|',end="")
			elif 2 in Ys:
				print ('\t   Y\t\t|',end="")
			else:
				print ('\t\t\t|',end="")
			if 3 in Xs:
				print ('\t   X\t\t')
			elif 3 in Ys:
				print ('\t   Y\t\t')
			else:
				print ('\t\t\t')

		else:
			print ('coming soon')

def getinput(Xs,Ys):
	x=input('Move position =')
	#print(type(x))
	x=int(x)
	#print(type(x))
	if x in Xs or x in Ys:
		print('Value used.Try again.')
		x=getinput(Xs,Ys) 
	elif x not in range(1,10):
		print("Invalid. Use between 1-9.Try again.")
		x=getinput(Xs,Ys)
	return x
Xs= []
Ys= []

move=0
print_board(Xs,Ys)
while move in range(9) :#Moves from 1 to 9
	print('Move =',move +1)
	if move%2==0:
		Xs.append(getinput(Xs,Ys))
		print_board(Xs,Ys)
		validate(Xs,Ys)
	else:
		Ys.append(getinput(Xs,Ys))
		print_board(Xs,Ys)
		validate(Xs,Ys)
	print ('X',Xs,"\nY",Ys)

	move+=1



print_board(Xs,Ys)
if move>=9:
	print("Draw\t"*3)