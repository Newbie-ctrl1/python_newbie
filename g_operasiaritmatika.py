#operasi aritmatika 

a = 10
b = 3

#operasi tambah +
hasil = a + b 
print (a,'+',b,"=",hasil) 

#operasi tambah -

hasil = a - b 
print (a,'-',b,"=",hasil) 

#operasi tambah *

hasil = a * b 
print (a,'*',b,"=",hasil) 

#operasi tambah /

hasil = a / b 
print (a,'/',b,"=",hasil) 

#operasi eksponen/pangkat **

hasil = a ** b 
print (a,'**',b,"=",hasil) 

#operasi modulus/sisa pembagian %

hasil = a % b 
print (a,'%',b,"=",hasil) 

#operasi floor division/hasil pembagian di bulatkan ke bawah //

hasil = a // b 
print (a,'//',b,"=",hasil) 

#prioritas operasi, operasi precedence

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z //x 
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, 'hasil',hasil)

#contoh simple

hasil = x + y * z
print( x,'+',y,'*',z,'=',hasil)

#perintah yang didahulukan
"""
1. ()
2. exponen **
3. perkalian dan teman teman * ,/ ,** ,% ,//
4. pertambahan dan pengurangan """

#contoh
hasil = (x + y) * z
print( '(' ,x,'+',y,')','*',z,'=',hasil)