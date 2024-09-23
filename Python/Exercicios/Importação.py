
print('===========================')
print(f'Calculadora de importação!')
print('===========================')
dolar=4.93
taxaicms=0.17
imposto=0.60
valor_inicial=float(input('Digite o valor bruto do item em reais conforme mostra no site!\n'))
#frete=str(input('Frete Incluso?'))
valor_dolar=valor_inicial/dolar
if valor_dolar>=50:
    taxaimposto=valor_dolar*imposto
else:
    taxaimposto=0

impostoliquido=(valor_dolar*taxaicms)+taxaimposto
valorfinal=valor_inicial+(impostoliquido*dolar)
print(f'O valor final do produto será de {valorfinal} Reais')
porcentagem_acrescimo = ((valorfinal - valor_inicial) / valor_inicial) * 100
print(f'Total de imposto foi de: {porcentagem_acrescimo}%')


