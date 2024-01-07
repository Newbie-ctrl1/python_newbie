# OPERATOR ASSIGMENT

a = 5 #ini adalah asigment
a = a + 1
print("nilai a =",a)
# operasi ditambah assigment
a += 1 # ARTINYA SAMA DENGAN a = a + 1
print("nilai a +=,   ""maka menjadi nilai =",a)
""" JUGA BERLAKU PADA ( +, - , * , /, %, //, ** ){umtuk keseluruhan aritmatika}"""

#OPERASI BITWISE
#OR { | }
c = True
print('\nnilai c =',c)
c |= False
print("nilai c |=,   ""maka menjadi nilai =",c)
c = False
print('nilai c =',c)
c |= False
print("nilai c |=,   ""maka menjadi nilai =",c)

''' BERLAKU PADA SELURUH OPERASI BITWISE { | , & , ^}[ OR , AND , XOR]'''

# SHIFT RIGHT DAN LEFT [GESER GESER]
d = 0b0100
print('nilai d = ',format(d,'04b'))
d >>= 2
print('nilai d >>=2 , nilai d menjadi =',format(d,'04b'))
d <<= 1
print('nilai d <<=1 , nilai d menjadi =',format(d,'04b'))
