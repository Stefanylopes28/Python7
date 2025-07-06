import json

def escrever_dados_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

def ler_dados_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            print("Dados lidos do arquivo JSON:")
            for chave, valor in dados.items():
                print(f"{chave}: {valor}")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")

pessoa = {
    "Nome": "Arthur",
    "Idade": 6,
    "Cidade": "Rio de Janeiro"
}

arquivo = 'pessoa.json'

escrever_dados_json(arquivo, pessoa)

ler_dados_json(arquivo)
