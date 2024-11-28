def contar_caracteres(string):
    # Inicializa um dicionário vazio para armazenar as contagens de caracteres
    contador = {}

    # Itera através de cada caractere na string
    for caractere in string:
        # Verifica se o caractere já está presente no dicionário contador
        if caractere in contador:
            # Incrementa o valor associado à chave
            contador[caractere] += 1
        else:
            # Adiciona a chave ao dicionário com valor inicial 1
            contador[caractere] = 1

    return contador


# Solicita entrada do usuário
entrada = input("Digite a string: ")
resultado = contar_caracteres(entrada)
print(resultado)
