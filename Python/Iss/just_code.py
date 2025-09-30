print("Bem-vindo à calculadora de Diárias")

quantidade_de_dias = int(input("Digite a quantidade de diárias: "))

# Caso de apenas 1 diária
if quantidade_de_dias == 1:
    diaria_str = input("Digite o valor da diária: ").replace(",", ".")
    diaria = float(diaria_str)
    diaria_final = diaria * 1.05
    print(f"O valor da diária total com ISS é de: R$ {diaria_final:.2f}")

# Caso com várias diárias
else:
    total = 0
    for dia in range(1, quantidade_de_dias + 1):
        diaria_str = input(f"Digite o valor da diária do dia {dia}: ").replace(",", ".")
        diaria = float(diaria_str)
        diaria_com_iss = diaria * 1.05
        total += diaria_com_iss
    print(f"O valor total das diárias com ISS é de: R$ {total:.2f}")
