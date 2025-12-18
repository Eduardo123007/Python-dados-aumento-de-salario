from datetime import date

nome = input("Digite seu nome: ")

print("Digite sua data de nascimento:")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

hoje = date.today()
idade = hoje.year - ano

if (hoje.month, hoje.day) < (mes, dia):
    idade -= 1

sexo = input("Digite seu sexo (M/F): ").upper()
while sexo != "M" and sexo != "F":
    sexo = input("Sexo inválido. Digite M ou F: ").upper()
    

cargo = input("Digite seu cargo: ")

salario = float(input("Digite o salário: "))

tempo_de_servico = int(input("Digite seu tempo de serviço (anos): "))

if tempo_de_servico >= 5:
    aumento = 0.10
elif tempo_de_servico >= 3:
    aumento = 0.05
elif tempo_de_servico > 1:
    aumento = 0.03
else:
    aumento = 0.0

novo_salario = salario + (salario * aumento)

print("\nDADOS DO FUNCIONÁRIO")
print(f"Nome: {nome}")
print(f"Data de nascimento: {dia:02d}/{mes:02d}/{ano}")
print(f"Idade: {idade} anos")
print(f"Sexo: {'Masculino' if sexo == 'M' else 'Feminino'}")
print(f"Cargo: {cargo}")
print(f"Salário atual: R$ {salario:.2f}")
print(f"Tempo de serviço: {tempo_de_servico} anos")
print(f"Novo salário: R$ {novo_salario:.2f}")