class Usuario:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
    
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, tiene de saldo: {self.balance_cuenta}")

    def transferir_dinero(self, amount, name_user):
        self.balance_cuenta -= amount
        name_user.balance_cuenta += amount