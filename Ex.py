import os
from collections import Counter
import collections
os.system('clear' if os.name == 'posix' else 'cls')
print("\n ______Menu______\n|1- Ex1;         |\n|2- Ex2;         |\n|3- Ex3;         |\n|4- Ex4;         |\n|5- Ex5;         |\n|6- Ex6;         |\n|7- Ex7;         |\n|8- Ex8;         |\n|9- Ex9;         |\n|10- Ex10;       |\n|11- Ex11;       |\n|12- Ex12;       |\n|13- Ex13;       |\n|14- Ex14;       |\n|15- Ex15;       |\n|16- Ex16;       |\n|17- Ex17;       |\n|18- Ex18;       |\n|19- Ex19;       |\n|20- Ex20;       |")
opc = int(input("\nEscolhe uma opção do menu: "))
if opc == 1:
    list = ["Simão","gostoso"]
    def MaxTamanho(x):
        return max(x)
    max = MaxTamanho(list)
    print("Frase: Simão gostoso, a maior palavra é:",max)
elif opc == 2:
    list = (100, "Simão", 1.0)
    a, b, c = list
    print(a)
    print(b)  
    print(c)
elif opc == 3:
    list = "Simão"
    contar = collections.Counter(list)
    print(contar)
elif opc == 4:
    list = ['simão','muito','gostoso']
    ordem = sorted(list)
    print(ordem)
elif opc  == 5:
    list = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
    lista= set(list)
    print(lista)
elif opc == 6:
    list = [("Simão", 16),("Jamie", 17), ("João", 99), ("Alexandre", 2), ("José", 35)]
    ordem = sorted(list, key=lambda x: x[1])
    print(ordem)
elif opc == 7:
    palavra = "simao"
    list = {letra: index  for index, letra in enumerate(palavra)}
    print(list)
elif opc == 8:
    numeros = [2, 5, 10]
    soma = sum([x for x in numeros if x % 2 == 0])
    print(soma)
elif opc == 9:
    pessoas = [{'nome': 'Simão', 'idade': 16, 'Trabalho': 'Estudante'},{'nome': 'ZéRic', 'idade': 45, 'Trabalho': 'Youtuber'},{'nome': 'KIKO', 'idade': 1.3, 'Trabalho': 'Destruir sofás'}]
    ordem = sorted(pessoas, key=lambda x: x['idade'])
    print(ordem)
#elif opc == 10:
elif opc == 11:
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numerospar = [num for num in numeros if num % 2 == 0]
    print(numerospar)
elif opc == 12:
    list1 = [1, 2, 3, 4, 5, 11, 0]
    list2 = [4, 2, 5, 6, 7, 8, 11]
    comun = [x for x in set(list1).intersection(list2)]
    print(comun)
elif opc == 13:  
    pessoas = [("Simão", 16),("Kiko", 1.3)]
    nomes = [nome for nome, idade in pessoas]
    idades = [idade for nome, idade in pessoas]
    print(nomes)
    print(idades)
elif opc == 14:
    import collections
    string = ["Simão", "é", "muito", "muito", "gostoso"]
    contar = (collections.Counter(string))
    print(contar.most_common())
#elif opc == 15:
elif opc == 16:
    pessoas = [{'nome': 'Simão', 'idade': 16, 'Trabalho': 'Estudante'},{'nome': 'ZéRic', 'idade': 45, 'Trabalho': 'Youtuber'},{'nome': 'KIKO', 'idade': 1.3, 'Trabalho': 'Destruir sofás'}]
    list = [x["nome"] for x in pessoas if x["idade"] > 30]
    print(list)
elif opc == 17:
    lista = [1,2,3,4,5]
    n = {x**2 for x in lista}
    print(n)
elif opc == 18:
    pessoas = [{'nome': 'Simão', 'idade': 16},{'nome': 'ZéRic', 'idade': 45},{'nome': 'KIKO', 'idade': 1.3}]
    ordem = sorted(pessoas, key=lambda x: x['nome'])
    print(ordem)
elif opc == 19:
    list = ["Simão", "é", "intelegente","E", "muito","Organizado"]
    lista = [x.lower() for x in list if x[0].lower() in "aeiou"]
    print(lista)
elif opc == 20:
    pessoas = [{'nome': 'Simão', 'idade': 16, 'Trabalho': 'Estudante'},{'nome': 'ZéRic', 'idade': 45, 'Trabalho': 'Youtuber'},{'nome': 'KIKO', 'idade': 1.3, 'Trabalho': 'Destruir sofás'}]
    list = [x for x in pessoas if x["idade"] > 30]
    print(list)
    
       