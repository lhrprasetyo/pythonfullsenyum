# ubahlah text PythonForTrainer menjadi : pYTHONfORtRAINER
text = input("Insert text : ")
out =[]
for i in text :
    txt = i
    if i.isupper():
        txt.lower()
    if i.islower():
        txt.upper
    out.append(txt)
print("".join(out))

