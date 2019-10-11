# total 94

all_ages = [8, 7, 9, 7, 10, 6]
soma = 0

for i in range(len(all_ages)):
    if i < len(all_ages) - 1:
        soma_age = all_ages[i + 1] + all_ages[i - 1]
        print(soma_age)
        soma += soma_age
    else:
        soma_age = all_ages[0] + all_ages[i - 1]
        print(soma_age)
        soma += soma_age
        
print(soma)