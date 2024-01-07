#operator bitwise, operasi binery, biner

a = 9
b = 5
#operasi bitwise OR { | }
c = a | b
print("\n========OR========")
print('nilai : ',a,"    binary =",format(a,'08b'))
print('nilai : ',b,"    binary =",format(b,'08b'))
print("--------------------------------{|}")
print('nilai : ',c,"    binary =",format(c,'08b'))

#operasi bitwise AND { & }
c = a & b
print("\n========AND========")
print('nilai : ',a,"    binary =",format(a,'08b'))
print('nilai : ',b,"    binary =",format(b,'08b'))
print("--------------------------------{&}")
print('nilai : ',c,"    binary =",format(c,'08b'))

#operasi bitwise XOR { ^ }
c = a & b
print("\n========XOR========")
print('nilai : ',a,"    binary =",format(a,'08b'))
print('nilai : ',b,"    binary =",format(b,'08b'))
print("--------------------------------{^}")
print('nilai : ',c,"    binary =",format(c,'08b'))

#operasi bitwise NOT { ~ }
c = ~a
print("\n========NOT========")
print('nilai : ',a,"    binary =",format(a,'08b'))
print("--------------------------------{~}")
print('nilai : ',c,"    binary =",format(c,'08b'))
print("--------------------------------{^}")
d = 0b0000001001 #untuk flip
e = 0b1111111111
print('nilai : ',e^d,"    binary =",format(e^d,'08b'))
# untuk flip juga bida pakai format ini
c = ~ b
print('\nNilai b:',b,' dalam bntk binary:', format(b, '08b'))
print("--------------------------------{&}")
print('Nilai c:',c,' dalam bntk binary:', format(c & 0xFF, '08b'))

# shifting
#shifting right (>>)
c =  a>>2
print("\n========>>========")
print('nilai : ',a,"    binary =",format(a,'08b'))
print("--------------------------------{>>}")
print('nilai : ',c,"    binary =",format(c,'08b'))
#shifting right (<<)
c =  a<<2
print("\n========<<========")
print('nilai : ',a,"    binary =",format(a,'08b'))
print("--------------------------------{<<}")
print('nilai : ',c,"    binary =",format(c,'08b'))
