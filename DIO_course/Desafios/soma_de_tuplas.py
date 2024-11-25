'''Desenvolva uma função em Python que recebe uma tupla de números
inteiros e retorna a soma de todos os elementos dessa tupla. A função
deve ser capaz de lidar com tuplas de qualquer tamanho, contanto que
todos os elementos sejam números inteiros. O objetivo é praticar a
manipulação de tuplas e a utilização de funções em Python.'''

'''
# No "TODO", abaixo: Crie a função 'soma_tupla' para receber uma tupla de números inteiros como argumento:
sum = 0
tupla = ()
def soma_tupla(tupla):
    for x in tupla:
        sum += x
    return sum(tupla)


if __name__ == "__main__":
    entrada = input()
    # No "TODO", abaixo: Defina tupla para receber os números inteiros:
    elementos = tupla(map(int, entrada.split()))

    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")
'''


# No "TODO", abaixo: Crie a função 'soma_tupla' para receber uma tupla de números inteiros como argumento:
def soma_tupla(tupla):
    return sum(tupla)


if __name__ == "__main__":
    entrada = input("Digite os números inteiros separados por espaço: ")
    # No "TODO", abaixo: Defina tupla para receber os números inteiros:
    elementos = tuple(map(int, entrada.split()))

    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")
