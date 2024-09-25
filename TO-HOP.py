	def toHop(n,k):
	    tuso = 1
	    mauso = 1
	    for i in range(n-k+1, n+1):
	        tuso *= i
	    for i in range(1, k+1):
	        mauso *= i
	    CKN = tuso // mauso
	    return CKN
	k = int(input("Nhập số nguyên k: "))
	n = int(input("Nhập số nguyên n: "))
	print("Kết quả:",toHop(n,k))
