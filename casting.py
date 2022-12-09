# mengubah suatu tipe data menjadi tipe data yang lain

# 1.Mengubah string menjadi number dan sebaliknya
# int()->Mengubah tipe data menjadi int
x='10'
print(type(x)) #mengecek tipe data sebuah variable
y='5'
x=int(x)
y=int(y)
z= x+y
print(z)

# 2.mengubah int menjadi float dan sebaliknya bisa
z = float(z)
print(z)

# 3.mengubah tipe data menjadi string, atau yang lainnya
z = str(z)
print(type(z))

# by default, tipe data yang dihasilkan oleh inputan adalah string 
# contoh:
a = input("a : ")
b = input("b : ")
print(a+b)