# criar funções para adicionar itens na agenda
phonebook = []

def add_item(name, phone_type, number):
    person = {
        "name": name,
        "telephones": [
            {
                "phone_type": phone_type,
                "number": number
            }
        ]
    }
    phonebook.append(person)

    print(phonebook)

def list_item(name, phone_type, number):
    for x in phonebook:
        print(x)
        
def delete_all(name, phone_type, number):
    if len(phonebook) != 0:
        person.clear()
        print('os contatos foram removidos')
        
def delete_item(name, phone_type, number):
    if len(phonebook) != 0:
        for x in phonebook:
            if x.name == name:
                print('deu certo')
        
    
        
