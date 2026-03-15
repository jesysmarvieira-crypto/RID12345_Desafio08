import json

# Configuração da Regra de Negócio
# No Azure, o custo médio é de $0.25 por unidade (DIU) por hora
PRECO_POR_DIU_HORA = 0.25

def calcular_monitoramento():
    try:
        # 1. Carregar os dados do arquivo JSON
        with open('dados_custos.json', 'r') as arquivo:
            dados = json.load(arquivo)

        print("="*50)
        print("SISTEMA DE MONITORAMENTO DE CUSTOS - AZURE DATA FACTORY")
        print("="*50)

        total_geral = 0

        # 2. Processar cada linha de log simulada
        for item in dados:
            nome_pipeline = item['pipeline']
            horas = item['duracao_horas']
            dius = item['diu_usada']

            # A fórmula mágica do custo
            custo_calculado = horas * dius * PRECO_POR_DIU_HORA
            total_geral += custo_calculado

            print(f"Pipeline: {nome_pipeline}")
            print(f" -> Consumo: {horas}h com {dius} DIUs")
            print(f" -> Custo Estimado: ${custo_calculado:.2f}")
            print("-" * 30)

        print(f"VALOR TOTAL ESTIMADO: ${total_geral:.2f}")
        print("="*50)

    except FileNotFoundError:
        print("Erro: O arquivo 'dados_custos.json' não foi encontrado!")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    calcular_monitoramento()