inserir01 = int(input("Informe Leitura Atual "))
inserir02 = int(input("Informe Leitura Anterior "))

# Calcula o valor do consumo em R$
consumo = (inserir01 - inserir02) * 0.834850

# Calcula o valor da Iluminação Pública
iluminacao_publica = consumo * 0.09342

# Calcula o valor Pis
pis = consumo * 0.00588

# Calcula o valor de Confins
confins = consumo * 0.02845

# Calcula o valor final da fatura
valor_final = consumo + iluminacao_publica + pis + confins

# Apresenta o resultado na tela
print("")
print("(Consumo Jan/2024)")
print("______________________________")

print(f"Valor em consumo  |R$ {consumo:.2f}  reais")
print(f"Iluminação Pública|R$  {iluminacao_publica:.2f}  reais")
print(f"Pis               |R$   {pis:.2f}  reais")
print(f"Confins           |R$  {confins:.2f}  reais")
print(f"Valor:            |R$ {valor_final:.2f}  reais")
print("______________________________")
