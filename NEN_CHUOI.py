chuoi = "aaabccccddda"
st = ""    
a = 1       # số kí tự trong dãy kí tự liên tiếp
n = len(chuoi)
chuoi = chuoi + "0" # cầm canh kí tự "0"
for i in range(n):
            if chuoi[i] == chuoi[i+1]: a = a + 1
            elif a == 1: st = st + chuoi[i]; #kết thúc dãy liên tiếp = nhau
            else:
                        st = st + chuoi[i] + str(a)
                        a = 1
print("Chuỗi nén:",st)
