A=[]
kata = input("masukkan kata : ")
for k in kata:
    A.append(k)
A.reverse()
B = "".join(A)
if kata == B :
    print("palindrom")
else :
    print("bukan palindrom")