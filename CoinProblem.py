
#COIN CHANGE PROBLEM
#compilar: python name.py

#Monto a juntar
C=11
#Denominacion de las monedas
W=[1,5,6,8]

#m requires len(w)+1 rows and c+1 columns
Matrix=[[]]
j, i = C+1, len(W)+1 
Matrix = [[0 for x in range(j)] for y in range(i)]# la llenamos con ceros

for r in range(1,len(W)+1):#filas
	for d in range(1,C+1):#columnas
		#Si no cabe
		if r == 1:#si la denominacion es de 1
			Matrix[r][d]=d
		elif W[r-1] > d:#si la denominacion es mayor
			Matrix[r][d] = Matrix[r-1][d]#la denominacion anterior
		else:#Si cabe
			Matrix[r][d] = min(Matrix[r-1][d], Matrix[r][d-W[r-1]] + 1)#comparamos el de arriba contra

print Matrix

print  'The minimum is: ' + str(Matrix[len(W)][C]) + ' of ' + str(W[len(W)-1])

#Knowing the elements inserted

XR=[0 for x in range(len(W))]
i=0
a=len(W)#renglon
b=C#columna

while(b>= 0):

	#print 'a: ' + str(a)
	#print 'b: ' + str(b)
	if Matrix[a][b] == Matrix[a-1][b] :
		if(a <0) :
			break
		else:
			a = a-1
	else:
		XR[a-1]=XR[a-1] + 1
		b= b - (W[a-1])

print 'LOS ELEMENTOS SON:'
for x in range(len(XR)):

	if XR[x] >= 0:
		print  str(XR[x]) + ' de ' + str(W[x]) + ', '
	






