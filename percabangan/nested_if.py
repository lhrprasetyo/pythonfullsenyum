nilai = float(input("Masukkan nilai anda : "))
# if nilai >=90:
#     print("Grade A")
# else:
#     if nilai >=80:
#         print("Grade B")
#     else :
#         if nilai >=70:
#             print("Grade C")
#         else :
#             if nilai >=60:
#                 print("Grade D")
#             else :
#                 if nilai >=50:
#                     print("Grade E")
#                 else :
#                     print("Anda tidak lulus")

# cara lebih cepat
if nilai >=90 and nilai <= 100:
    print("Grade A")
elif nilai >=80 and nilai < 90:
    print("Grade B")
elif nilai >=70 and nilai < 80:
    print("Grade C")
elif nilai >=60 and nilai < 70:
    print("Grade D")
elif nilai >=0 and nilai <50:
    print("Tidak Lulus")
else:
    print("invalid input!")