	fi = open("SVM.INP","r")
	fo = open("SVM.OUT","w",encoding="utf-8")
	x = int(fi.readline())
	k,n = map(int,fi.readline().split())
	def kTra(x): # Xây dựng hàm tính tổng
	    return sum(list(map(int, str(x)))) == 9
	def toHop(n,k):
	    tuso = 1
	    mauso = 1
	    for i in range(n-k+1, n+1):
	        tuso *= i
	    for i in range(1, k+1):
	        mauso *= i
	    CKN = tuso // mauso
	    return kTra(CKN)
	if toHop(n,k):
	    fo.write("Số viên mãn")
	else:
	    fo.write("No")
	fi.close()
	fo.close()
