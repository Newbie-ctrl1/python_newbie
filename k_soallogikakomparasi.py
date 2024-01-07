print("\n",5*"=","LATIHAN SOAL LOGIKAN DAN KOMPARASI",5*"=","\n")

# 1. Masukan angka
#-----0++++++5-------8++++++11------#
#PENEYELESAIAN(penggabungan)


inputuser = float(input("====Masukan angka yang bernilai====\n lebih dari 0 dan kurang dari 5\n ==Atau==\n Lebih dari 8 dan kurang dari 11\n"))

#---0+++
isLebihDari = inputuser >0
print("lebih dari       = ",isLebihDari)
#+++5----
isKurangDari = inputuser <5
print("Kurang dari dari = ",isKurangDari)
#---8+++
isLebihDari = inputuser >8
print("lebih dari       = ",isLebihDari)
#+++11----
isKurangDari = inputuser <11
print("Kurang dari dari = ",isKurangDari)

isCorrect = (isLebihDari and isKurangDari)and(isLebihDari or isKurangDari)
print("jadi angka yang anda masukan =  ",isCorrect)


#+++++++0-----------5++++++++++8---------11+++++
#PENEYELESAIAN
#(potongan )
inputuser = float(input("====Masukan angka yang bernilai====\n Kurang dari 0 atau Lebih dari dari 5\n ==dan==\n Kurang dari 8 atau Lebih dari 11\n"))

#+++0----
isKurangDari = inputuser <0
print("Kurang dari       = ",isKurangDari)
#---5++++
isLebihDari = inputuser >5
print("Lebih dari        = ",isLebihDari)
#++++8----
isKurangDari = inputuser <8
print("Kurang dari       = ",isKurangDari)
#----11++++
isLebihDari = inputuser >11
print("Lebih dari        = ",isLebihDari)

isCorrect = (isKurangDari and isLebihDari) or (isKurangDari and isLebihDari)
print("jadi angka yang anda masukan =  ",isCorrect)


print("\n========== IF STATMENT =========\n")
# jurus if statment
x = float(input("masukkan angka : "))
if (x>0 and x<5) or (x>8 and x<11) :
	print(True)
else :
	print(False)
	
x = float(input("masukkan angka : "))
if (x<0 or x>5) and (x<8 or x>11) :
	print(True)
else :
	print(False)
	
    #JAWABAN YANG BENAR
	