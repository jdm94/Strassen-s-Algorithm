
def new_m(p, q): # create a matrix filled with 0s
	matrix = [[0 for row in range(p)] for col in range(q)]
	return matrix



def partition(matrix):
	a = matrix
	b = matrix
	c = matrix
	d = matrix
	while(len(a) > len(matrix)/2):
		a = a[:len(a)/2]
		b = b[:len(b)/2]
		c = c[len(c)/2:]
		d = d[len(d)/2:]
	while(len(a[0]) > len(matrix[0])/2):
		for i in range(len(a[0])/2):
			# print i
			a[i] = a[i][:len(a[i])/2]
			b[i] = b[i][len(b[i])/2:]
			c[i] = c[i][:len(c[i])/2]
			d[i] = d[i][len(d[i])/2:]
	return a,b,c,d
		
def Add_M(M1,M2):
	if(type(M1) == int):
		return M1 + M2
	D = []
	for i in range(len(M1)):
		C = []
		for j in range(len(M1[i])):
			C.append(M1[i][j] + M2[i][j])
		D.append(C)
	return D



def Sub_M(M1,M2):
	if(type(M1) == int):
		return M1 - M2
	D = []
	for i in range(len(M1)):
		C = []
		for j in range(len(M1[i])):
			C.append(M1[i][j] - M2[i][j])
		D.append(C)
	return D


def FetchResult(P1,P2,P3,P4,P5,P6,P7):
	# print P1
	C11 = Add_M(P5,Add_M(Sub_M(P4,P2),P6))
	C12 = Add_M(P1,P2)
	C21 = Add_M(P3,P4)
	C22 = Sub_M(Add_M(P1,P5),Add_M(P3,P7))
	N = len(C11)
	
	C = new_m(N*2,N*2)
	for i in range(N):
		for j in range(N):
			C[i][j] = C11[i][j]
			C[i][j+N] = C12[i][j]
			C[i+N][j] = C21[i][j]
			C[i+N][j+N] = C22[i][j]
	return C
	

	
def strassen(A,B,N):
	if(N == 1):
		C = [[0]]
		C[0][0] = A[0][0] * B[0][0]
		return C
	else:
		a,b,c,d = partition(A)
		e,f,g,h = partition(B)

		P1 = strassen(a,Sub_M(f,h),N/2)
		P2 = strassen(Add_M(a,b),h,N/2)
		P3 = strassen(Add_M(c,d),e,N/2)
		P4 = strassen(d,Sub_M(g,e),N/2)
		P5 = strassen(Add_M(a,d),Add_M(e,h),N/2)
		P6 = strassen(Sub_M(b,d),Add_M(g,h),N/2)
		P7 = strassen(Sub_M(a,c),Add_M(e,f),N/2)

		# print P1,P2,P3
		C = FetchResult(P1,P2,P3,P4,P5,P6,P7)
		return C

a = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
b = [[5,5,5,5],[6,6,6,6],[7,7,7,7],[8,8,8,8]]
print strassen(a,b,4)