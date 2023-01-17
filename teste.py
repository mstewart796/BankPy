from models.cliente import Cliente
from models.conta import Conta

felicity: Cliente = Cliente('Fel Jone', 'Fel@gmail', '123.23', '01/01/2000')
ang: Cliente = Cliente('Ang Jol', 'and@gmail', '456.45', '01/01/1990')

# print(felicity)
# print(ang)

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(ang)

# print(contaf)
# print(contaa)
