
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
        else:
            print("La cantidad que desea depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.balance:
                self.balance -= cantidad
            else:
                print("lamentablemente tiene fondos insuficientes.")
        else:
            print("La cantidad que desea retirar debe ser positiva.")

    def Cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota

    def mostrar_detalles(self):
        print(f"El numero de cuenta es : {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: {self.balance:.2f}")

cuenta = CuentaBancaria("0350788173", ["Felipe Guzman", "Fernanda Ortega"], 100.000)

cuenta.mostrar_detalles()

cuenta.depositar(45.000)
print("\nDespués del depósito:")
cuenta.mostrar_detalles()

cuenta.retirar(50.000)
print("\nDespués del retiro:")
cuenta.mostrar_detalles()

cuenta.Cuota_manejo()
print("\nDespués de aplicar la cuota de manejo:")
cuenta.mostrar_detalles()
