import random

def sorteio_mega_sena():
    numeros_sorteados = random.sample(range(1, 61), 6)
    return sorted(numeros_sorteados)

def sorteio_lotofacil():
    numeros_sorteados2 = random.sample(range(1, 25), 15)
    return sorted(numeros_sorteados2)

# Realizando o sorteio
resultado = sorteio_mega_sena()
resultado2 = sorteio_lotofacil()
print(f"Números sorteados megasena:{resultado}")
print(f"Números sorteados lotofacil:{resultado2}")


