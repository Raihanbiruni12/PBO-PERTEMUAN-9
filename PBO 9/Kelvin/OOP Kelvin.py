class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_Kelvin(self):
        val = self.suhu
        return val

    def get_Reamur(self):
        val = 4/9 * (self.get_Kelvin() - 32)
        return val

    def get_fahrenheit(self):
        val = 5/9 * (self.get_Kelvin() - 32) + 273.15
        return val
    
    def get_celcius(self):
        val = 5/9 * (self.get_Kelvin() - 32) 
        return val

suhu = float(input("Masukkan suhu dalam Kelvin: "))
R = Kelvin(suhu)
val = R.get_Kelvin()

R_in_Reamur = R.get_Reamur()
C = R.get_celcius()
F = R.get_fahrenheit()

print(str(val) + " Kelvin sama dengan:")
print(str(R_in_Reamur) + " Reamur")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
