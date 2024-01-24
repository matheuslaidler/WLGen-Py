import string
import time
import sys
import random

# Criação de tabelas de tradução para substituir caracteres
table1 = str.maketrans('aioO', '@100')
table2 = str.maketrans('aeioOs', '43100$')
table3 = str.maketrans('aeiou', 'AEIOU')
table4 = str.maketrans('IilLsS', '1111$$')
# Cada tabela é um mapeamento de um conjunto de caracteres 
# para outro conjunto.
# Por exemplo, 'aioO' é mapeado para '@100' na primeira tabela

# Agrupando todas as tabelas em uma lista
list_tables = [table1, table2, table3, table4]
# A ideia do agrupamento serve para facilitar o uso posterior.


def write_variations(line, number, number_sequence, modo):
    """
    Esta função gera variações de uma linha de entrada, aplicando várias transformações
    e adicionando uma sequência numérica.
    """
    variations = []

    for table in list_tables:
        formatted_line = line.translate(table)

        # Adiciona a sequência numérica em algumas variações
        variations.extend(generate_formatted_lines(formatted_line, number, modo))

        # Adiciona a sequência numérica em algumas variações, substituindo a sequência do ano
        variations.extend(generate_formatted_lines(formatted_line, number_sequence, modo))

    return variations

def generate_formatted_lines(formatted_line, number, modo):
    """
    Esta função gera várias variações de uma linha formatada, adicionando um número
    e aplicando várias transformações de string.
    """
    if modo == '2':  # Modo avançado
        number = str(random.randint(0, 9999))  # Gera um número aleatório

    return [
        f"{formatted_line}{number}\n",
        f"{number}{formatted_line}\n",
        f"{formatted_line}@{number}\n",
        f"{number}@{formatted_line}\n",
        f"{formatted_line}@{number}\n".upper(),
        f"{number}@{formatted_line}\n".upper(),
        f"{formatted_line}{number}\n".upper(),
        f"{number}{formatted_line}\n".upper(),
        f"{formatted_line}@{number}\n".lower(),
        f"{number}@{formatted_line}\n".lower(),
        f"{formatted_line}{number}\n".lower(),
        f"{number}{formatted_line}\n".lower(),
        f"{formatted_line}@{number}\n".capitalize(),
        f"{number}@{formatted_line}\n".capitalize(),
        f"{formatted_line}{number}\n".capitalize(),
        f"{number}{formatted_line}\n".capitalize(),
        f"{formatted_line}@{number}\n".title(),
        f"{number}@{formatted_line}\n".title(),
        f"{formatted_line}{number}\n".title(),
        f"{number}{formatted_line}\n".title(),
        f"{formatted_line}@{number}\n".swapcase(),
        f"{number}@{formatted_line}\n".swapcase(),
        f"{formatted_line}{number}\n".swapcase(),
        f"{number}{formatted_line}\n".swapcase(),
    ]

def brute_force(number, input_lines, number_sequence, modo):
    """
    Esta função aplica a força bruta para gerar todas as possíveis variações
    de cada linha de entrada.
    """
    for line in input_lines:
        wordlist.write(line)
        line = line.rstrip('\n')
        line2 = f"{line}{number}\n"
        wordlist.write(line2)
        line2 = f"{number}{line}\n"
        wordlist.write(line2)
        line2 = f"{line}@{number}\n"
        wordlist.write(line2)
        line2 = f"{number}@{line}\n"
        wordlist.write(line2)
        variations = write_variations(line, number, number_sequence, modo)
        wordlist.writelines(variations)

def main():
    print("Bem-vindo a criação de wordlist automatizada!\n")
    print(" Este script cria uma wordlist de combinações\n de cada palavra digitada, isto significa que\n as palavras não se misturam.\n A lista irá reescrever cada palavra de forma\n diversa, com letras maiúsculas e minúsculas,\n substituição/adição de palavra por caractere\n especial e até com ou sem números se desejar\n\n Depois de digitar todas as palavras, aperte\n Enter p/ encerrar e escolher se quer números\n\n Este script cria uma wordlist de combinações\n Escolher o modo da wordlist é importante. \n No modo Simples você usará a sequência numé-\n rica fornecida antes/depois da palavra.\n A sequência numérica é como um ano.\n Já no modo Avançado os números serão aleató-\n rios estando antes ou depois da palvra\n sem precisar colocar sequência numérica.\n\n Matheus Laidler - WLGen script lab v0.1\n\n\n")

    input_lines = []
    while True:
        line = input("[-] Digite uma palavra: ")
        if line.lower() == '':
            break
        input_lines.append(line + '\n')

    if not input_lines:
        print("Nenhuma palavra fornecida. Encerrando o programa.\n")
        sys.exit(1)

    number_sequence = input("\n[-] Digite uma sequência numérica (ou deixe em branco): ")

    modo = input("\n[-] Escolha o modo de execução:\n  [1] Modo Simples\n  [2] Modo Avançado\n")

    if modo not in {'1', '2'}:
        print("Modo inválido. Encerrando o programa.\n")
        sys.exit(1)

    print("*" * 38)
    print("**** Geração de Wordlist ****")
    print("*" * 38)

    brute_force('', input_lines, number_sequence, modo)

    print("\n[+][+] Geração concluída. Confira 'wordlist.txt'!")
    wordlist.close()

if __name__ == '__main__':
    try:
        wordlist = open('wordlist.txt', 'w')
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        sys.exit(1)
    main()
