def exibir():
    print(f'O Total foi de: {resultado}!')



print("Bem vindo a calculadora básica")
valor1=int(input('Entre com o primeiro valor: '))
operador=input('Selecione o operador (+ - * /)')
valor2=int(input('Entre com o segundo valor: '))

if operador=='+':
    resultado=valor1+valor2
    exibir()
if operador=='-':
    if valor1>valor2:
        resultado=valor1-valor2
        exibir()
    else:
        resultado=valor2-valor1
        exibir()
if operador=='*':
    resultado=valor1*valor2
    exibir()
if operador=='/':
    if valor1>valor2:
        resultado=valor1/valor2
        exibir()
    else:
        resultado=valor2/valor1
        exibir()
