'''fahrenheit ke kelvin'''

print("\nTUGAS KONVERSI FAHRENHEIT\n" )

fahrenheit = float(input('masukan suhu fahreinheit ='))
print ("suhu fahreinhet adalah = ",fahrenheit)

#celsius
celsius = ((5/9) * fahrenheit) - 32
print ("suhu celsius adalah = ",celsius)
 
#reamur
reamur = ((4/9)*fahrenheit) - 32 
print ("suhu reamur adalah = ",reamur)

#kelvin
kelvin = ((fahrenheit - 32) * 5/9) + 273
print ("suhu kelvin adalah = ",kelvin)

'''KELVIN KE FAHRENHEIT'''

print("\nTUGAS KONVERSI KELVIN\n")

kelvin = float (input('masukan suhu kelvin ='))
print ("suhu kelvin adalah = ",kelvin)

#celsius
celsius = kelvin - 273
print ("suhu celsius adalah = ",celsius)
 
#reamur
reamur = ((4/5) * kelvin) - 273
print ("suhu reamur adalah = ",reamur)

#kelvin
fahrenheit = (( kelvin - 273.15) * 9/5) + 32  
print ("suhu fahrenheit adalah = ",fahrenheit)



