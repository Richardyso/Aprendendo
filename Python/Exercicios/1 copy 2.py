operacoes = {'+': lambda x, y: x + y, '-': lambda x, y: abs(x - y), '*': lambda x, y: x * y, '/': lambda x, y: x / y if y != 0 else "Erro: Divisão por zero não é permitida."}

print("Bem vindo a calculadora básica")
valor1 = int(input('Entre com o primeiro valor: '))
operador = input('Selecione o operador (+, -, *, /): ')
valor2 = int(input('Entre com o segundo valor: '))

resultado = operacoes.get(operador, lambda x, y: "Erro: Operador inválido. Por favor, escolha +, -, *, ou /.")(valor1, valor2)
print(f"O resultado foi: {resultado}")
