# belajar & latihan komparasi dan logika

# membuat gabungan area rentang dari angka

# soal +++++++++3----------10++++++++++

# cara penyelesaianya

#+++++++++++++3-----
inputuser = float(input(" Masukan angka yang bernilai\nKurang dari 3\n=====ATAU=====\nLebih dari 10\n"))

isKurangDari = inputuser <3            #operasi komparasi
print("Kurang dari 3 = ",isKurangDari)
#------------10++++

isLebihDari = inputuser >10            #operasi komparasi
print("Lebih dari 10 = ", isLebihDari)

# or (untuk penggabungan)
isCorrect = isKurangDari or isLebihDari  #operasi logika
print("Angka yang anda masukan = ",isCorrect)

# soal -----------3+++++++++++++10-----------

print("\n",10*"=",'\n')

inputuser = float(input(" Masukan angka yang bernilai\nlebih dari 3\n=====DAN=====\nKurang dari 10\n"))
 
 #-----------3++++++++++++
isLebihDari = inputuser>3
print ("lebih dari 3 > = ",isLebihDari)

#++++++++10---------
isKurangDari = inputuser <10
print ("Kurang dari 3 > = ",isKurangDari)

isCorrect = isLebihDari and isLebihDari
print("Angka yang anda masukan = ",isCorrect)


print(30*"=") #alat baru,,bwahahahaa






