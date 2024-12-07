 inflacao = 0.038

  # Define as faixas salariais e os percentuais de aumento
  faixas = {
      280: 0.20,  # Até R$ 280,00 - 20%
      700: 0.15,  # Entre R$ 280,01 e R$ 700,00 - 15%
      1500: 0.10, # Entre R$ 700,01 e R$ 1500,00 - 10%
      float("inf"): 0.05  # Acima de R$ 1500,00 - 5%
  }

  # Calcula o aumento baseado na faixa salarial
  for limite, percentual in faixas.items():
    if salario <= limite:
      aumento = salario * percentual
      break

  # Calcula o novo salário
  novo_salario = salario + aumento

  # Calcula o valor do aumento real
  aumento_real = aumento * (1 - inflacao)

  # Retorna os valores calculados
  return salario, percentual * 100, aumento, novo_salario, aumento_real

# Solicita o salário do colaborador
salario = float(input("Digite o salário do colaborador: R$ "))

# Calcula o reajuste e exibe os resultados
salario_inicial, percentual, aumento, novo_salario, aumento_real = calcular_reajuste(salario)

print("\nResultados:")
print(f"1. Salário antes do reajuste: R$ {salario_inicial:.2f}")
print(f"2. Aumento aplicado: {percentual:.2f}%")
print(f"3. Valor do aumento: R$ {aumento:.2f}")
print(f"4. Novo salário: R$ {novo_salario:.2f}")
print(f"5. Valor do aumento real: R$ {aumento_real:.2f}")