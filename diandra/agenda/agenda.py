#discenir qual comando que foi escolhido (add, edit, delete, list)
import sys
from functions import add_item

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

choice = sys.argv[1]
name = sys.argv[2]
phone_type = sys.argv[3]
number = sys.argv[4]

if choice == "add":
    print("será adicionado")
    add_item(name, phone_type, number)
elif choice == "edit":
    print('será editado')
elif choice == "list":
    print('listar elementos')
elif choice == "delete":
    print("deletar elementos")
else:
    print("comando inválido")

