import os
from collections import Counter
import collections
while True:
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\n ______Menu______\n|1- Ex1;         |\n|2- Ex2;         |\n|3- Ex3;         |\n|4- Ex4;         |\n|5- Ex5;         |\n|6- Ex6;         |\n|7- Ex7;         |\n|8- Ex8;         |\n|9- Ex9;         |\n|10- Ex10;       |\n|11- Ex11;       |\n|12- Ex12;       |\n|13- Ex13;       |\n|14- Ex14;       |\n|15- Ex15;       |\n|16- Ex16;       |\n|17- Ex17;       |\n|18- Ex18;       |\n|19- Ex19;       |\n|20- Ex20;       |\n|21- Sair;       |")
    opc = int(input("\nEscolhe uma opção do menu: "))
    if opc == 1:
        list = ["Simão","gostoso"]
        def MaxTamanho(x):
            return max(x)
        max = MaxTamanho(list)
        print(max)
        exit()
    elif opc == 2:
        list = (100, "Simão", 1.0)
        a, b, c = list
        print(a)
        print(b)  
        print(c)
        exit()
    elif opc == 3:
        list = "Simão"
        contar = collections.Counter(list)
        print(contar)
        exit()
    elif opc == 4:
        list = ['simão','muito','gostoso']
        ordem = sorted(list)
        print(ordem)
        exit()
    elif opc  == 5:
        list = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
        lista= set(list)
        print(lista)
        exit()
    elif opc == 6:
        list = [("Simão", 16),("Jamie", 17), ("João", 99), ("Alexandre", 2), ("José", 35)]
        ordem = sorted(list, key=lambda x: x[1])
        print(ordem)
        exit()
    elif opc == 7:
        palavra = "simao"
        list = {letra: index  for index, letra in enumerate(palavra)}
        print(list)
        exit()
    elif opc == 8:
        numeros = [2, 5, 10]
        soma = sum([x for x in numeros if x % 2 == 0])
        print(soma)
        exit()
    elif opc == 9:
        pessoas = [{'nome': 'Simão', 'idade': 16, 'Trabalho': 'Estudante'},{'nome': 'ZéRic', 'idade': 45, 'Trabalho': 'Youtuber'},{'nome': 'KIKO', 'idade': 1.3, 'Trabalho': 'Destruir sofás'}]
        ordem = sorted(pessoas, key=lambda x: x['idade'])
        print(ordem)
        exit()
    #elif opc == 10:
    elif opc == 11:
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        numerospar = [num for num in numeros if num % 2 == 0]
        print(numerospar)
        exit()
    elif opc == 12:
        list1 = [1, 2, 3, 4, 5, 11, 0]
        list2 = [4, 2, 5, 6, 7, 8, 11]
        comun = [x for x in set(list1).intersection(list2)]
        print(comun)
        exit()
    elif opc == 13:  
        pessoas = [("Simão", 16),("Kiko", 1.3)]
        nomes = [nome for nome, idade in pessoas]
        idades = [idade for nome, idade in pessoas]
        print(nomes)
        print(idades)
        exit()
    elif opc == 14:
        string = ["Simão", "é", "muito", "muito", "gostoso"]
        contar = (collections.Counter(string))
        print(contar.most_common())
        exit()
    #elif opc == 15:
    elif opc == 16:
        pessoas = [{'nome': 'Simão', 'idade': 16, 'Trabalho': 'Estudante'},{'nome': 'ZéRic', 'idade': 45, 'Trabalho': 'Youtuber'},{'nome': 'KIKO', 'idade': 1.3, 'Trabalho': 'Destruir sofás'}]
        list = [x["nome"] for x in pessoas if x["idade"] > 30]
        print(list)
        exit()
    elif opc == 17:
        lista = [1,2,3,4,5]
        n = {x**2 for x in lista}
        print(n)
        exit()
    elif opc == 18:
        pessoas = [{'nome': 'Simão', 'idade': 16},{'nome': 'ZéRic', 'idade': 45},{'nome': 'KIKO', 'idade': 1.3}]
        ordem = sorted(pessoas, key=lambda x: x['nome'])
        print(ordem)
        exit()
    elif opc == 19:
        list = ["Simão", "é", "intelegente","E", "muito","Organizado"]
        lista = [x.lower() for x in list if x[0].lower() in "aeiou"]
        print(lista)
        exit()
    elif opc == 20:
        pessoas = [{'nome': 'Simão', 'idade': 16, 'Trabalho': 'Estudante'},{'nome': 'ZéRic', 'idade': 45, 'Trabalho': 'Youtuber'},{'nome': 'KIKO', 'idade': 1.3, 'Trabalho': 'Destruir sofás'}]
        list = [x for x in pessoas if x["idade"] > 30]
        print(list)
        exit()
    elif opc == 21:
        exit()
    else:
        print()
    
    
       