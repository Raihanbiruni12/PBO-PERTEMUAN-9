def fahrenheit_ke_celcius(suhu):
    """
    Mengkonversi suhu Fahrenheit ke Celcius.

    Argumen:
      suhu: Suhu dalam satuan Fahrenheit.

    Mengembalikan:
      Suhu dalam satuan Celcius.
    """
    return 5 / 9 * (suhu - 32)

def fahrenheit_ke_reamur(suhu):
    """
    Mengkonversi suhu Fahrenheit ke Reamur.

    Argumen:
      suhu: Suhu dalam satuan Fahrenheit.

    Mengembalikan:
      Suhu dalam satuan Reamur.
    """
    return 4 / 9 * (suhu - 32)

def fahrenheit_ke_kelvin(suhu):
    """
    Mengkonversi suhu Fahrenheit ke Kelvin.

    Argumen:
      suhu: Suhu dalam satuan Fahrenheit.

    Mengembalikan:
      Suhu dalam satuan Kelvin.
    """
    return 5 / 9 * (suhu - 32) + 273

def main():
    # Mendapatkan input pengguna
    suhu_fahrenheit = float(input("Masukkan suhu dalam satuan Fahrenheit: "))

    # Mengkonversi dan mencetak suhu
    celcius = fahrenheit_ke_celcius(suhu_fahrenheit)
    reamur = fahrenheit_ke_reamur(suhu_fahrenheit)
    kelvin = fahrenheit_ke_kelvin(suhu_fahrenheit)

    print(f"Suhu dalam Celcius: {celcius:.2f}")
    print(f"Suhu dalam Reamur: {reamur:.2f}")
    print(f"Suhu dalam Kelvin: {kelvin:.2f}")

if __name__ == "__main__":
    main()
