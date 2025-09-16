# Coletando os dados da pessoa
nome = input("Digite seu nome: ")
endereco = input("Digite seu endereço: ")
idade = int(input("Digite sua idade: "))
sexualidade = input("Digite sua sexualidade: ")
altura = float(input("Digite sua altura (em metros, ex: 1.75): "))
peso = float(input("Digite seu peso (em kg, ex: 70.5): "))

# ---

# Calculando a relação entre peso e altura
# Vamos chamar o resultado de IMC (Índice de Massa Corporal) para maior clareza
# Embora a lógica seja uma divisão simples, essa é a base do cálculo do IMC
try:
    imc = peso / (altura * altura) # O cálculo correto do IMC é peso dividido por altura ao quadrado
except ZeroDivisionError:
    print("Erro: A altura não pode ser zero.")
    exit()

# ---

# Verificando as condições e imprimindo a mensagens
if imc > 25:
    print(f"\n{nome}, você está com sobrepeso .")
elif imc >= 19 and imc <= 24:
    print(f"\n{nome}, você está com peso ideal.")
else:
    print(f"\n{nome}, sua condição não se encaixa nas categorias de peso ideal ou sobrepeso.")

# ---
print(f"Seu IMC é de: {imc:.2f}")