# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.
p = float(input("Preço: "))
Im = (p * (12/100))
pIm = (p + Im)
print(f"Preço com imposto: {pIm}")
