program = 'Python For Trainer'

# mengubah capital menjadi  uppercase
print(program)
print(program.upper())

# mengubah string menjadi huruf kecil
print(program.lower())

# menghilangkan spasi pada awal dan akhir
text = " Hello, World "
print(f"{text.strip()}")

# casting menjadi list
text_list = list(text)
print(f"{text_list}")

# mengubah list menjadi string 
jadi_string = "".join(text_list)
print(f"Jadi String : {jadi_string.strip()}")