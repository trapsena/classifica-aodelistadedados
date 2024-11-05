import math
list = [10, 44, 33, 22, 50, 3, 13, 8, 11, 11, 57, 90, 91]
x = int(input("Qual o valor que deseja pesquisar: "))
for i in list:
    if x == i:
            print("Valor encontrado")
            print(i) 
            break
    else:
          print(f"Valor {x} não encontrado na lista")

list.sort()



def pesquisa_binaria(lista_de_numeros , valor_pesquisado):
    primeiro_indice = 0
    tamanho = len(lista_de_numeros)
    ultimo_indice = tamanho - 1
    indice_elemento_do_meio = (primeiro_indice + ultimo_indice) // 2
    elemento_do_meio = lista_de_numeros[indice_elemento_do_meio]

    encontrado = True
    while encontrado:
        if primeiro_indice == ultimo_indice:
            if elemento_do_meio != valor_pesquisado:
                encontrado = False
                return "Não aparece na lista"

        elif elemento_do_meio == valor_pesquisado:
            return f"{elemento_do_meio} encontrado na posição {indice_elemento_do_meio}"

        elif elemento_do_meio > valor_pesquisado:
            nova_posicao = indice_elemento_do_meio - 1
            ultimo_indice = nova_posicao
            indice_elemento_do_meio = (primeiro_indice + ultimo_indice) // 2
            elemento_do_meio = lista_de_numeros[indice_elemento_do_meio]
            if elemento_do_meio == valor_pesquisado:
                return f"{elemento_do_meio} encontrado na posição {indice_elemento_do_meio}"

        elif elemento_do_meio < valor_pesquisado:
            nova_posicao = indice_elemento_do_meio + 1
            primeiro_indice = nova_posicao
            ultimo_indice = tamanho - 1
            indice_elemento_do_meio = (primeiro_indice + ultimo_indice) // 2
            elemento_do_meio = lista_de_numeros[indice_elemento_do_meio]
            if elemento_do_meio == valor_pesquisado:
                return f"{elemento_do_meio} encontrado na posição {indice_elemento_do_meio}"




bin= int(input("Qual o valor que deseja pesquisar(pelo metodo de binario): "))
print(pesquisa_binaria(list , bin))

def busca_salto(lista, alvo):
    n = len(lista)
    passo = int(math.sqrt(n))  # Define o tamanho do salto
    anterior = 0

    # Pula os blocos até encontrar um intervalo onde o alvo possa estar
    while lista[min(passo, n)-1] < alvo:
        anterior = passo
        passo += int(math.sqrt(n))
        if anterior >= n:
            return -1  # Não encontrado

    # Realiza busca linear no bloco identificado
    for i in range(anterior, min(passo, n)):
        if lista[i] == alvo:
            return i  # Elemento encontrado

    return -1  # Não encontrado

jump= int(input("Qual o valor que deseja pesquisar(pelo metodo de jump): "))
indice = busca_salto(list, jump)

if indice != -1:
    print(f"Elemento encontrado no índice {indice}")
else:
    print("Elemento não encontrado")


def pesquisa_fibonacci(lista, alvo):
    # Inicializa números de Fibonacci
    fib_m2 = 0  # (m-2)-ésimo número de Fibonacci
    fib_m1 = 1  # (m-1)-ésimo número de Fibonacci
    fib_m = fib_m2 + fib_m1  # m-ésimo número de Fibonacci

    n = len(lista)
    
    # Encontra o menor número de Fibonacci maior ou igual ao tamanho da lista
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    # Marca o início da seção verificada
    offset = -1

    # Enquanto houver elementos para verificar
    while fib_m > 1:
        # Verifica se fib_m2 é uma posição válida
        i = min(offset + fib_m2, n - 1)

        # Se o alvo é maior, mova a janela de busca para a direita
        if lista[i] < alvo:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i

        # Se o alvo é menor, mova a janela de busca para a esquerda
        elif lista[i] > alvo:
            fib_m = fib_m2
            fib_m1 -= fib_m2
            fib_m2 = fib_m - fib_m1

        # Alvo encontrado
        else:
            return i

    # Verifica o último elemento
    if fib_m1 and offset + 1 < n and lista[offset + 1] == alvo:
        return offset + 1

    # Alvo não encontrado
    return -1


alvo = int(input("Digite o número que deseja encontrar(FIBO): "))
resultado = pesquisa_fibonacci(list, alvo)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}")
else:
    print("Elemento não encontrado")


