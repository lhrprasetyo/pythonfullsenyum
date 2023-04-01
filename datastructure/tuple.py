laptop = ("HP","Asus","Dell","Apple","Acer","Dell")
print(laptop)
print(laptop[2])
laptop = list(laptop)
laptop[2] = "ROG"
laptop = tuple(laptop)
print(laptop)
print(laptop[2])

# index()
print(laptop.index("ROG"))
print(laptop.index("Dell"))

# count 
print(laptop.count("Dell"))


mytuple = ("max",19,"28")

# memebedakan tuple dan string :
tuple1 = ('budi')
print(f" tipe data variabel tuple1 adalah :{type(tuple1)}")
tuple2 = ('budi',)
print(f" tipe data variabel tuple2 adalah :{type(tuple2)}")
print(mytuple)

exTuple = ("a","p","p","l","e")
rearrange = []
for i in exTuple:
    rearrange.append(i)
b = "".join(rearrange)
print(b)

