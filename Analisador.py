# Projeto: Analisador de Gastos em Python
print("--- BEM VINDO AO ANALISADOR DE DADOS FINANCEIROS---")
#Entrada de dados
salario = float(input("digite o valor do seu salario mensal: "))
aluguel = float(input("Quanto voce paga de aluguel? "))
alimentacão = float(input("Quanto gasta com alimentacão? "))
outros = float(input("total de outros gastos: "))
#Cálculos (Engenharia de Dados Básica)
total_gastos = aluguel + alimentacão + outros
saldo_final = salario - total_gastos
#Exibição dos resultados
print("\n--- RESUMO FINANCEIRO ---")
print(f"Salário Bruto:R${salario:.2f}")
print(f"Total de Gastos: R${total_gastos:.2f}")
if saldo_final > 0: 
    print(f"Parabéns! Sobrou R${saldo_final:.2f} para investir.")
elif saldo_final == 0:
   print("Cuuidado! Você gastou exatamente o que ganha.")
else:
   print(f"Atenção! Você está no negativo: R${saldo_final:.2f}")