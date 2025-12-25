birth_year = input('What is your birth year? ')
# age = 2025 - birth_year — kalau pake code ini bakal error, krn birth_year dianggap sebagai teks.  harusnya jadi integer.
age = 2025 - int(birth_year)
print(age)

#coba mendapatkan jenis variabel
print("birth_year type is :" + str(type(birth_year)))
print("age type is :" + str(type(age))) 

#ype harus dikonversi jadi str agar bisa di concat
