# cara input data user

# input data
data = input ("masukan data = ")
print ("data = ", data , "tipe data = ", type(data))
# data yang dimasukan pasti akan menjadi data string

# jika ingin mengambil int 
data_int = int (input("masukan angka = "))
print("angka = ",data_int, "tipe = ", type(data_int))

#jika ingin mengambil float

data_float = float (input("masukan angka = "))
print("angka = ",data_float, "tipe = ", type(data_float))

#jika kita ingin memasukan data boolean
#jadikan integer dulu baru ke boolean

biner = bool(int(input("masukan nilai boolean =")))
print("data = ",biner, "type = ",type(biner))
   