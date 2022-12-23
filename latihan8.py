#Latihan konversi satuan temperature
#program konversi celcius ke satuan lain

print("\nProgram Konversi Temperatur\n")

celcius = float (input("Masukan Suhu Dalam Celcius : "))
print("suhu adalah",celcius,"Celcius")

#Reamurr
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur,"Reamur")

#Farenheit
farenheit = ((9/5) * celcius) + 32
print("suhu dalam farenheit adalah ",farenheit,"Farenheit")

#Kelvin
kelvin = celcius + 273
print("suhu dalam Kelbin adalah",kelvin,"Kelvin")