import statistics

def analisar_tempo_execucao(caminho_arquivo):
    tempos = []

    try:
        with open(caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
            
                if 'Execution time:' in linha:
                    partes = linha.split('Execution time: ')
                    if len(partes) > 1:
                        tempo_str = partes[1].replace('s', '').strip()
                        tempo = float(tempo_str)
                        tempos.append(tempo)

        if tempos:
            media = statistics.mean(tempos)
            desvio_padrao = statistics.stdev(tempos)
            print(f"\nMédia do tempo de execução: {media:.2f} segundos")
            print(f"Desvio padrão: {desvio_padrao:.2f} segundos\n")
        else:
            print("\nNenhum tempo de execução encontrado no arquivo.\n")

    except FileNotFoundError:
        print(f"\nArquivo '{caminho_arquivo}' não encontrado. Verifique o nome e o caminho.\n")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}\n")

analisar_tempo_execucao('dados_log.txt')

