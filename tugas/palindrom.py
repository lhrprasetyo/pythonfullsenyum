kata = input("masukkan kata : ")
A=[]
for k in kata:
    A.append(k)
A.reverse()
B = "".join(A)
if kata == B :
    print("palindrom")
else :
    print("bukan palindrom")