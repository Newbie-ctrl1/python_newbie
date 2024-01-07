# operasi logika atau kebenaran (tabel kebenaran)
# NOT, OR, AND, XOR
 
# NOT (akan selalu kebalikan)
print("======NOT======")
a = True
print('data boolean = ',a)
# memasukan NOT
print("\n======NOT======\n")
a = True
c = not a
print('data a = ',a)
print('----- NOT')
print('data c = ',c)

# memasukan NOT
print("======NOT======")
a = False
c = not a
print('data a = ',a)
print('----- NOT')
print('data c = ',c)

# OR (jika salah satu "True" maka hasilnya "True")
# harus ada dua object
print("\n====== OR ======\n")
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True 
c = a or b
print(a,'OR',b,' =',c)
a = True
b = False
c = a or b
print(a,' OR',b,'=',c)
a = True
b = True
c = a or b
print(a,' OR',b,' =',c)

# AND (jika salah satu "FALSE" maka hasilnya "FALSE")
# harus ada dua object
print("\n====== AND ======\n")
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)
a = True
b = True
c = a and b
print(a,' AND',b,' =',c)

# XOR ( akan "True" jika salah satu "True",sisanya adalah "False")
# harus ada dua object
# TANDA XOR ( ^ )
print("\n====== XOR ======\n")
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c)
