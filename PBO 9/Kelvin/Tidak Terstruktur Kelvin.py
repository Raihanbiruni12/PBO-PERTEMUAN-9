def kelvin_ke_reamur(suhu):
    """Konversi suhu dari Kelvin ke Reamur.

    Args:
      suhu: Suhu dalam satuan Kelvin.

    Returns:
      Suhu dalam satuan Reamur.
    """
    return (suhu - 273.15) * 4 / 5

def kelvin_ke_fahrenheit(suhu):
    """Konversi suhu dari Kelvin ke Fahrenheit.

    Args:
      suhu: Suhu dalam satuan Kelvin.

    Returns:
      Suhu dalam satuan Fahrenheit.
    """
    return (suhu - 273.15) * 9 / 5 + 32

def kelvin_ke_celcius(suhu):
    """Konversi suhu dari Kelvin ke Celcius.

    Args:
      suhu: Suhu dalam satuan Kelvin.

    Returns:
      Suhu dalam satuan Celcius.
    """
    return suhu - 273.15

def main():
    suhu_kelvin = float(input("Masukkan suhu dalam satuan Kelvin: "))

    reamur = kelvin_ke_reamur(suhu_kelvin)
    fahrenheit = kelvin_ke_fahrenheit(suhu_kelvin)
    celcius = kelvin_ke_celcius(suhu_kelvin)

    print("Suhu dalam satuan Reamur:", reamur)
    print("Suhu dalam satuan Fahrenheit:", fahrenheit)
    print("Suhu dalam satuan Celcius:", celcius)

if __name__ == "__main__":
    main()
