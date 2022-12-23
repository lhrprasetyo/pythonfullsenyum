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
