# Função hash simples baseada na soma dos valores ASCII dos caracteres do nome do arquivo
def funcao_hash(nome, tamanho):
    return sum(ord(char) for char in nome) % tamanho

# Função para inicializar a tabela hash com um tamanho fixo
def inicializar_tabela(tamanho):
    return {i: [] for i in range(tamanho)}

# Função para adicionar um arquivo à tabela hash
def adicionar_arquivo(tabela, tamanho, nome, caminho, tamanho_arquivo):
    indice = funcao_hash(nome, tamanho)
    for arquivo in tabela[indice]:
        if arquivo["nome"] == nome:
            print(f"Erro: O arquivo '{nome}' já existe.")
            return
    tabela[indice].append({
        "nome": nome,
        "caminho": caminho,
        "tamanho": tamanho_arquivo
    })
    print(f"Arquivo '{nome}' adicionado com sucesso.")

# Função para buscar um arquivo pelo nome
def buscar_arquivo(tabela, tamanho, nome):
    indice = funcao_hash(nome, tamanho)
    for arquivo in tabela[indice]:
        if arquivo["nome"] == nome:
            return arquivo
    return None

# Função para remover um arquivo pelo nome
def remover_arquivo(tabela, tamanho, nome):
    indice = funcao_hash(nome, tamanho)
    for arquivo in tabela[indice]:
        if arquivo["nome"] == nome:
            tabela[indice].remove(arquivo)
            print(f"Arquivo '{nome}' removido com sucesso.")
            return
    print(f"Erro: Arquivo '{nome}' não encontrado.")

# Função para listar todos os arquivos na tabela hash
def listar_arquivos(tabela):
    arquivos = []
    for lista in tabela.values():
        arquivos.extend(lista)
    return arquivos

# Exemplo de uso
tamanho_tabela = 10
tabela_hash = inicializar_tabela(tamanho_tabela)

# Adicionando arquivos
adicionar_arquivo(tabela_hash, tamanho_tabela, "relatorio.pdf", "/documentos/relatorio.pdf", 1024)
adicionar_arquivo(tabela_hash, tamanho_tabela, "foto.jpg", "/imagens/foto.jpg", 2048)
adicionar_arquivo(tabela_hash, tamanho_tabela, "dados.csv", "/planilhas/dados.csv", 512)
adicionar_arquivo(tabela_hash, tamanho_tabela, "backup.zip", "/backup/backup.zip", 4096)

# Buscando um arquivo
arquivo = buscar_arquivo(tabela_hash, tamanho_tabela, "dados.csv")
if arquivo:
    print("\nArquivo encontrado:")
    print(f"Nome: {arquivo['nome']}, Caminho: {arquivo['caminho']}, Tamanho: {arquivo['tamanho']} KB")
else:
    print("\nArquivo 'dados.csv' não encontrado.")

# Removendo um arquivo
print("\nRemovendo 'foto.jpg':")
remover_arquivo(tabela_hash, tamanho_tabela, "foto.jpg")

# Listando todos os arquivos restantes
print("\nListando todos os arquivos:")
for arquivo in listar_arquivos(tabela_hash):
    print(f"Nome: {arquivo['nome']}, Caminho: {arquivo['caminho']}, Tamanho: {arquivo['tamanho']} KB")
