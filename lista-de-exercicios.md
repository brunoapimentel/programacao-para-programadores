## EXERCÍCIOS DE LÓGICA

---

### EXERCÍCIO 01
Considere o vetor abaixo:

`numeros = [8, 7, 9, 7, 10, 6]`

Escreva um algorítmo que some o valor no número antecessor e sucessor de cada item do vetor.

---

### EXERCÍCIO 02
João e Maria fizeram uma prova na escola. Crie um algorítmo que corrija a prova dos alunos comparando as respostas com o gabarito. Em seguida, imprima a nota de cada aluno considerando o peso de cada resposta correta.


JOÃO | MARIA | GABARITO | PESO
--- | --- | --- | ---
1 - C | 1 - C | 1 - A | Vale 3 pontos
2 - A | 2 - D | 2 - A | Vale 2 pontos
3 - D | 3 - D | 3 - B | Vale 1 ponto
4 - B | 4 - D | 4 - A | Vale 1 ponto
5 - D | 5 - D | 5 - A | Vale 3 pontos

---

### EXERCÍCIO 03
Crie um programa que receba o total de vendas abaixo. O Bruno ganhará 5% do total de vendas da Ana, Diandra e Nico, sendo que eles também ganharão 5% do total de vendas de seus funcionários.  


 **Ex:**

|                             |           BRUNO           |                              |
| --------------------------- |:-------------------------:| ---------------------------- |
|          ANA R$ 300         |       DIANDRA R$ 450      |          NICO R$ 500         |
| BIA R$ 100    CAMILA R$ 350 | MAGA R$ 200  FÁBIO R$ 210 |  LUCAS R$ 150   VINI R$ 100  |

---

### EXERCÍCIO 04
Crie um algorítmo de busca binária que localize um número no vetor abaixo:

`numeros = [2, 7, 9, 10, 31, 50, 140, 328, 1024]`

---

### EXERCÍCIO 05
Crie um algorítmo de bubble sort no vetor desordenado abaixo:

`numeros = [2, 90, 43, 21, 5, 10]`

---

### EXERCICIO 06

**Capricho - Quiz Vocacional**

- Coach
- Startupeiro
- Gourmetizador
- Blogueirinho


1- Na sua carreira, você prefere:


| Alternativa   | Peso Coach | Peso Startupeiro  | Peso Gourmet | Peso Blogueirinho  |
|    :----:   |    :----:   |    :----:   |    :----:   |    :----:   |
| Ajudar as pessoas chegarem nos seus objetivos      | 3  | 1  | 0  | 1  |
| Resolver problemas que ninguém resolve    |  0  | 3  | 3  | 0  |
| Ser positivo todos os dias   |  3  | 1  | 1  | 2 |
| Ser reconhecido por todos   |  0  | 2  | 2  | 3 |

<br>
2- No seu dia a dia, como você age com as pessoas:


| Alternativa   | Peso Coach | Peso Startupeiro  | Peso Gourmet | Peso Blogueirinho  |
|    :----:   |    :----:   |    :----:   |    :----:   |    :----:   |
| Você aconselha todo mundo      | 3  | 0  | 0  | 2  |
| Você é um bom ouvinte    |  0  | 1  | 3  | 1  |
| Você toma iniciativa   |  1  | 3  | 2  | 1 |
| Você analisas todas as opções     |  0  | 1  | 3  | 1 |

<br>
3- Se você fosse um animal, você seria:


| Alternativa   | Peso Coach | Peso Startupeiro  | Peso Gourmet | Peso Blogueirinho  |
|    :----:   |    :----:   |    :----:   |    :----:   |    :----:   |
| Um papagaio      | 3  | 2  | 0  | 2  |
| Um leão      |  0  | 3  | 2  | 2 |
| Uma formiga     |  1  | 2  | 1  | 3 |
| Um flamingo     |  1  | 1  | 3  | 1 |

<br>

**Respostas realizadas:**

> Eric [b, d, d] -  Gourmetizador

> Roger [a, b, a] -   Coach

> Nicao [b, c, c] -   Blogueirinho/Startupeiro (empate)

---

### EXERCICIO 07
a) Refatore o exercício da pirâmide de forma que seja feito através de uma função.
<br>
b) Como continuação do exercício do quizz, busque transformar o resultado obtido em porcentagem. Por exemplo: João é 58% gourmet.

---

### EXERCICIO 08
Criar uma agenda telefônica, com um CRUD básico feito com python puro.

Exemplo:

```
python3 agenda.py add "Roger Groger" "Xaomi" "(11) 9123123-1231232"
python3 agenda.py list "Rog"
add [nome] [identificador] [numero]
edit [busca] [identificador] [numero]
list
list [busca]
delete [busca]
```
