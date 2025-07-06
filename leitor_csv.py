import csv

def ler_e_mostrar_csv(nome_arquivo):
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            
            print(f"{'Nome':<20} {'Idade':<6} {'Cidade':<20}")
            print('-' * 50)
            
            for linha in leitor:
                nome = linha['Nome']
                idade = linha['Idade']
                cidade = linha['Cidade']
                print(f"{nome:<20} {idade:<6} {cidade:<20}")
                
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso:
ler_e_mostrar_csv('pessoas.csv')
