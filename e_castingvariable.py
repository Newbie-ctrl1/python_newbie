#casting data adalah merubah tipe data ke tipe yang lain
#kita belajar casting
#tipe data = int, float, str, bool
 

#PERUBAHAN INTEGER (SATUAN)
print("====INTEGER====")

data_int = 9
print("data = ", data_int, "-type",type (data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ", data_float, "-type",type (data_float))
print("data = ", data_str, "-type",type (data_str))
print("data = ", data_bool, "-type",type (data_bool))

#PERUBAHAN FLOAT (DESIMAL)

print("====float====")

data_float = 9.9
print("data = ", data_float, "-type",type (data_float))

data_int =int(data_float) # data integr akan dibulakan kebawah
data_str = str(data_float)
data_bool = bool(data_float) #kalo boolean jika data bernilai 0 maka false begitu sebaliknya
print("data = ", data_int, "-type",type (data_int))
print("data = ", data_str, "-type",type (data_str))
print("data = ", data_bool, "-type",type (data_bool))

#tipe data bolean ( true/false)

print("====boolean====")


data_bool = False
print("data = ", data_bool, "-type",type (data_bool))

data_float = float(data_bool)
data_str   = str(data_bool) #jika yang dimasukan false/true menjadi karakter
data_int   = int(data_bool)
print("data = ", data_float, "-type",type (data_float))
print("data = ", data_str, "-type",type (data_str))
print("data = ", data_int, "-type",type (data_int))


#tipe data : string (kharakter )

print("====string====")


data_str = 10
print("data = ", data_str, "-type",type (data_str))

data_float = float(data_str) #string harus angka
data_str   = str(data_str) #string harus angka
data_int   = int(data_str) #sting akan false jika kosong
print("data = ", data_float, "-type",type (data_float))
print("data = ", data_int, "-type",type (data_int))
print("data = ", data_bool, "-type",type (data_bool))
