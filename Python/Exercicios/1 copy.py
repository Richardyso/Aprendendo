print("Bem vindo a calculadora básica")
valor1=int(input('Entre com o primeiro valor: '))
operador=input('Selecione o operador (+ - * /)')
valor2=int(input('Entre com o segundo valor: '))

if operador=='+':
    resultado=valor1+valor2
    print(f'O Total foi de: {resultado}!')
if operador=='-':
    if valor1>valor2:
        resultado=valor1-valor2
        print(f'O total foi de: {resultado}')
    else:
        resultado=valor2-valor1
        print(f'O total foi de: {resultado}')
if operador=='*':
    resultado=valor1*valor2
    print(f'O total foi de: {resultado}')
if operador=='/':
    if valor1>valor2:
        resultado=valor1/valor2
        print(f'O total foi de: {resultado}')
    else:
        resultado=valor2/valor1
        print(f'O total foi de: {resultado}')



# Sugerido pelo gpt

print("Bem-vindo à calculadora básica")
valor1 = float(input('Entre com o primeiro valor: '))
operador = input('Selecione o operador (+, -, *, /): ')
valor2 = float(input('Entre com o segundo valor: '))

if operador == '+':
    resultado = valor1 + valor2
elif operador == '-':
    resultado = valor1 - valor2
elif operador == '*':
    resultado = valor1 * valor2
elif operador == '/':
    if valor2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        resultado = valor1 / valor2
else:
    print("Operador inválido. Por favor, selecione +, -, *, ou /.")

if 'resultado' in locals():
    print(f'O total é: {resultado}')
