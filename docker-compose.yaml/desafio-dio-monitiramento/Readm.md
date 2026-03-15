# Monitoramento de custos - Azure Data Factory

Este repositório contém uma solução de **Data Engineering** para o monitoramento e cálculo de custos de pipelines no **Azure Data Factory (ADF)***.

##Descrição do Projeto
Oobejtivo deste projeto é extrair dados de execução (logs)de pipelines e aplicar regras de negócio para calcular o custo operacional baseado em **DIUS (Data Integration Units)** e tempo de execução.

> **Nota:** Devido a restrições de crédito na nuvem, este projeto utiliza um ambiente de **simulação (Mocking)**.
Os logs de execução foram emulados em formasto JSON, seguindo o padrão do Azure Monitor, e processados via Python no VS Code.

# Tecnologias e Ferramnetas * **Python**: Para processamneto e cálculo dos dados.
* **JSON**: Para simulação dos logs de origem (Raw Data).
* **Vs Code**: Ambiente de desenvolvimento.
* **Git/Github**: Controle de versão e portifólio.

## Regra de Negócio Aplicada
O custo foi calculado seguindo a extimativa padrão do Microsoft Azure:
* **Custo** = (Duração em Horas) x (DIUs Utilizadas) x $0.25

## Como Executar
1. Clone o repositório
2. Certifique-se de ter o Python instalado.
3. Execute o comando: 'python processar-custos.py'