print('VAMOS CALCULAR')
ganhohora = float(input('Quanto você ganhou por hora? '))
horadia = float(input('Quantas horas você trabalhou por dia? '))
pordia=(horadia * ganhohora)
brutomes=(pordia*30)

irenda=float(11/100)
inss=float(8/100)
sindicato=float(5/100)
liquido1=float(irenda*brutomes)
liquido2=float(inss*brutomes)
liquido3=float(sindicato*brutomes)
print('Então, por dia você ganhou: R$',pordia)
print('No mês o valor bruto foi:R$',brutomes)
print('Nesse mês você pagou de IRRF:R${}'.format(liquido1))
print('Nesse mês você pagou de INSS:R${}'.format(liquido2))
print('Nesse mês você pagou de Sindicato:R${}'.format(liquido3))
print('SEU SALÁRIO LÍQUIDO DO MÊS FOI:R$', brutomes-liquido1-liquido2-liquido3)
print('Enquanto isso os descontos foram:')
print('De IRRF foi de:R$',liquido1)
print('De INSS foi de:R$',liquido2)
print('De Sindicato foi de:R$',liquido3)
print('Descontos somados', liquido1+liquido2+liquido3)






print('VAMOS CALCULAR')
ganhohora = float(input('Quanto você ganhou por hora? '))
horadia = float(input('Quantas horas você trabalhou por dia? '))
pordia = horadia * ganhohora
brutomes = pordia * 30

irenda = 0.11
inss = 0.08
sindicato = 0.05

liquido1 = irenda * brutomes
liquido2 = inss * brutomes
liquido3 = sindicato * brutomes

print('Então, por dia você ganhou: R$', pordia)
print('No mês o valor bruto foi: R$', brutomes)
print(f'Nesse mês você pagou de IRRF: R${liquido1:.2f}')
print(f'Nesse mês você pagou de INSS: R${liquido2:.2f}')
print(f'Nesse mês você pagou de Sindicato: R${liquido3:.2f}')

descontos = liquido1 + liquido2 + liquido3
salario_liquido = brutomes - descontos

print(f'SEU SALÁRIO LÍQUIDO DO MÊS FOI: R${salario_liquido:.2f}')
print('Enquanto isso os descontos foram:')
print(f'De IRRF foi de: R${liquido1:.2f}')
print(f'De INSS foi de: R${liquido2:.2f}')
print(f'De Sindicato foi de: R${liquido3:.2f}')
print('Descontos somados:', descontos)
