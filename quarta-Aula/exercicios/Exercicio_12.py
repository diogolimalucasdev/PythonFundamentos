# Três amigos jogaram na loteria.Caso eles ganhem,o prêmio deve ser repartido proporcionalmente
# ao valor que cada um deu para a realização da aposta.Faça um programa que leia quanto cada apostador
# investiu,o valor do prêmio,e imprima quanto cada um ganharia do prêmio com base no valor investido.
valor_premio = int(input("Digite o valor do premio: "))
primeiro_amigo = int(input("1ºamigo:  Digite o valor investido na aposta: "))
segundo_amigo = int(input("2ºamigo:  Digite o valor investido na aposta: "))
terceiro_amigo = int(input("3ºamigo:  Digite o valor investido na aposta: "))

soma = primeiro_amigo + segundo_amigo + terceiro_amigo

media_primeiroAmigo = round(primeiro_amigo / soma, 2)

media_segundo_amigo = round(segundo_amigo / soma, 2)

media_terceiro_amigo = round(terceiro_amigo / soma, 2)



print(f"A soma total foi {soma}")

print(f"O primeiro amigo investiu {round(media_primeiroAmigo ,2)}% e tem direito a \n"
      f" {valor_premio * media_primeiroAmigo}R$")

print(f"O Segundo amigo investiu {round(media_segundo_amigo , 2)}% etem direito a \n"
      f" {round(valor_premio * media_segundo_amigo, 2)}R$")

print(f"O terceiro amigo investiu {round(media_terceiro_amigo , 2)}% e tem direito a \n"
      f"{round(valor_premio * media_terceiro_amigo,2 )}R$")




