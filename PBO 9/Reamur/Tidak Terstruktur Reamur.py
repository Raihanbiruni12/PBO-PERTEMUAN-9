def reamur_ke_celcius(suhu):
  """Konversi suhu dari Reamur ke Celcius.

  Args:
    suhu: Suhu dalam satuan Reamur.

  Returns:
    Suhu dalam satuan Celcius.
  """

  return suhu * 4 / 9


def reamur_ke_fahrenheit(suhu):
  """Konversi suhu dari Reamur ke Fahrenheit.

  Args:
    suhu: Suhu dalam satuan Reamur.

  Returns:
    Suhu dalam satuan Fahrenheit.
  """

  return suhu * 9 / 5 + 32


def reamur_ke_kelvin(suhu):
  """Konversi suhu dari Reamur ke Kelvin.

  Args:
    suhu: Suhu dalam satuan Reamur.

  Returns:
    Suhu dalam satuan Kelvin.
  """

  return suhu + 273


def main():
  suhu = float(input("Masukkan suhu dalam satuan Reamur: "))

  reamur = reamur_ke_celcius(suhu)
  fahrenheit = reamur_ke_fahrenheit(suhu)
  kelvin = reamur_ke_kelvin(suhu)

  print("Suhu dalam satuan Celcius:", reamur)
  print("Suhu dalam satuan Fahrenheit:", fahrenheit)
  print("Suhu dalam satuan Kelvin:", kelvin)


if __name__ == "__main__":
  main()
