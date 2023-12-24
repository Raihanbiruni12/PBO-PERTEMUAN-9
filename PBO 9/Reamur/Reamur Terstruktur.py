print("Konversi Suhu Reamur")

# Fungsi Konversi
def get_celcius(suhu):
    return 5/9 * (float(suhu_Reamur) - 32)

def get_Kelvin(suhu):
    return 4/9 * (float(suhu_Reamur) - 32)

def get_fahrenheit(suhu):
    return 5/9 * (float(suhu_Reamur) - 32) + 273

# Entry
suhu_Reamur = input("Masukkan suhu dalam Reamur: ")

# Menggunakan Fungsi Konversi
C = get_celcius(suhu_Reamur)
K = get_Kelvin(suhu_Reamur)
F = get_fahrenheit(suhu_Reamur)

# Output
print(suhu_Reamur + " Reamur sama dengan ")
print(str(C) + " Celcius")
print(str(K) + " Kelvin")
print(str(F) + " Fahrenheit")
