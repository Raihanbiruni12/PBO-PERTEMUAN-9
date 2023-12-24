print("Konversi Suhu Kelvin")

# Fungsi Konversi
def get_celcius(suhu):
    return 5/9 * (float(suhu_Kelvin) - 32)

def get_reamur(suhu):
    return 4/9 * (float(suhu_Kelvin) - 32)

def get_fahrenheit(suhu):
    return 5/9 * (float(suhu_Kelvin) - 32) + 273

# Entry
suhu_Kelvin = input("Masukkan suhu dalam Kelvin: ")

# Menggunakan Fungsi Konversi
C = get_celcius(suhu_Kelvin)
R = get_reamur(suhu_Kelvin)
F = get_fahrenheit(suhu_Kelvin)

# Output
print(suhu_Kelvin + " Kelvin sama dengan ")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
print(str(F) + " Fahrenheit")
