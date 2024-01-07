
# tipe data adalh macam" data yang bisa dipakai dipython
# a = 10, a adalah variable dengan nilai 10

# macam" tipe data di python

#tipe data : angka satuan (integer) (1,2,3,4,5,,dst)
#tanpa ada desimal atau yang lain"""

data_integer = 1
print ("data : ",data_integer)
print("- bertipe : ",type(data_integer))

#tipe data : angka dengan koma (float)

data_float = 1.5
print ("data : ",data_float)
print("- bertipe : ",type(data_float))

# tipe data : kumpulan karakter (stringdata_string)

data_string = " ucup 10" 
print ("data : ",data_string)
print("- bertipe : ",type(data_string))

#tipe data : biner true/false (boolean)

data_bool = True
print ("data : ",data_bool)
print("- bertipe : ",type(data_bool))

## tipe data khusus 

#bilangan kompleks (untuk bilangan imajiner(khusus matematika))

data_complex = complex(5,6)
print ("data : ",data_complex)
print("- bertipe : ",type(data_complex))

# tipe data mengambil dari data c (jika data python sudah tidak ada)

from ctypes import c_double
data_c_double = c_double (10.5)
print ("data : ", data_c_double)
print ("-bertipe : ", type(data_c_double))