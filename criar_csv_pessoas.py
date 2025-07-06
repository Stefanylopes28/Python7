import csv

def escrever_dados_csv(nome_arquivo, dados):

    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        colunas = ['Nome', 'Idade', 'Cidade']
        escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

        escritor.writeheader()
        escritor.writerows(dados) 

pessoas = [
    {'Nome': 'Ana', 'Idade': 28, 'Cidade': 'Rio de Janeiro'},
    {'Nome': 'Bruno', 'Idade': 35, 'Cidade': 'São Paulo'},
    {'Nome': 'Carla', 'Idade': 22, 'Cidade': 'Belo Horizonte'},
]

escrever_dados_csv('pessoas.csv', pessoas)

print("Arquivo 'pessoas.csv' criado com sucesso!")
