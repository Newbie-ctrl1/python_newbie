# operasi komparasi

## setiap operasi komparasi adalah boolean
# < ,> ,>= ,<= ,== ,!=,is ,is not

a = 4
b = 2

#lebih besar dari >
print("---- lebih besar dari > ----")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

#kurang dari <
print("---- kurang dari < ----")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)
# lebih sama dengan dari >=
print(" ---- lebih sama dengan dari >= ----")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)
# kurang dari sama dengan <=
print("----- kurang dari sama dengan <= ------")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)
# sama dengan dari ==
print("---- sama dengan dari == ----")
hasil = a == 3
print(a,'==',3,'=',hasil)
hasil = b == 3
print(b,'==',3,'=',hasil)
hasil = b == 2
print(b,'==',2,'=',hasil)
# tidak sama dengan dari !=
print("---- tidak sama dengan dari != ----")
hasil = a != 3
print(a,'!=',3,'=',hasil)
hasil = b != 3
print(b,'!=',3,'=',hasil)
hasil = b != 2
print(b,'!=',2,'=',hasil)

# "is" = membandingkan memory/object
# "is" sebagai komparasi object
# "type(x)" fungsinya ubruk mencari kelas object
# "id(x)" untuk mencari addresnya atau IDnya
# "hex(id(x))" fungsinya mencari hex addres (c++)
# ***** "(x)" adalah nama variable ******
# contoh x = 1 . "(X)" menjadi sbuah variable pemanggil saja

print("====mencari addrees====")
x = 5 # ini adalah assigment membuat object
y = 5
print('print nilai x = ',x,'id = ' ,hex(id(x)))
print('print nilai x = ',y,'id = ' ,hex(id(y)))

# "is" untuk membandingkan object
hasil = x is y #membandingkan object
print("hasil x is y =" , hasil)

# "is not" untuk membandingkan object
hasil = x is not y
print("x is not y = ", hasil)