#Importando o módulo necessário
import random
#Gerando a lista principal
listaNumerica = [random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50)]
#Tava com preguiça de apagar 10 itens manualmente então criei esse loop pra reduzir a 50 termos.
while len(listaNumerica) > 50:
    listaNumerica.pop()
print(listaNumerica)
#Exercitando List Comprehension
listaDeNumerosPares = [num for num in listaNumerica if (num % 2 == 0) == True]
listaDeNumerosImpares = [num for num in listaNumerica if (num % 2 == 0) == False]
#Análise da composição da lista principal
print(f"{len(listaNumerica)} números no total na lista \'listaNumerica\'")
print(f"{len(listaDeNumerosPares)} números pares na lista \'listaNumerica\'")
print(f"{len(listaDeNumerosImpares)} números ímpares na lista \'listaNumerica\'")
print(f"Então, a quantidade de números pares corresponde a {((len(listaDeNumerosPares)/len(listaNumerica)) * 100):.1f}% do total de números e, por conseguinte, a quantidade de números ímpares corresponde a {100-(((len(listaDeNumerosPares)/len(listaNumerica)))*100):.1f}% do total de números")