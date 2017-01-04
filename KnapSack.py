
#KNAPSACK PROBLEM

#compilar: python name.py

#Capacidad de la mochila
C=20
#Pesos de los objetos
W=[9,5,4,3,2]
#Beneficios de los Objetos
B=[10,8,5,4,3]
#m requires len(w)+1 rows and c+1 columns
Matrix=[[]]
j, i = C+1, len(W)+1 #11 columns, 5 rows
Matrix = [[0 for x in range(j)] for y in range(i)]# la llenamos con ceros



for r in range(1,len(W)+1):#filas
	for d in range(1,C+1):#columnas
		#Si no cabe
		if W[r-1]>d:
			Matrix[r][d]=Matrix[r-1][d]#a la hora de acceder
		else:
		#Si cabe
			Matrix[r][d]=max(Matrix[r-1][d], Matrix[r-1][d-W[r-1]] + B[r-1])

print Matrix

print  'The maximun is: ' 
print  Matrix[len(W)][C]

#Knowing the elements inserted

XR=[0 for x in range(len(W))]
b=C #columa
#a= fila
for a in range(len(W),0,-1):
	
	if Matrix[a-1][b] == Matrix[a][b] :
		XR[a-1]=0
	else:	
		XR[a-1]=1

	b= C - (W[a-1]*XR[a-1])



print 'LOS ELEMENTOS SON:'
for x in range(len(XR)):

	if XR[x]== 1:
		print str(W[x]) + ','
	






