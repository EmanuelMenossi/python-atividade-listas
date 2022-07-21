lista = ['', '', '', ['', '', '', ]]
km = 500
preco = 4.90

lista[0] = (input("Digite o nome do primeiro carro: "))
lista[3][0] = int(input("Digite quantos KM o carro faz por Litros: "))
lista[1] = (input("Digite o nome do segundo carro: "))
lista[3][1] = int(input("Digite quantos KM o carro faz por Litros: "))
lista[2] = (input("Digite o nome do terceiro carro: "))
lista[3][2] = int(input("Digite quantos KM o carro faz por Litros: "))

print('========================================Emanuel Menossi=======================================')
print('----------------------------------------------------------------------------------------------')
print("O primeiro carro é o " + lista[0])
print("E faz ", lista[3][0], " KM por litro")
print('----------------------------------------------------------------------------------------------')
print("O segundo carro é o " + lista[1])
print("E faz ", lista[3][1], " KM Por litro")
print('----------------------------------------------------------------------------------------------')
print("O terceiro carro é o " + lista[2])
print("E faz ", lista[3][2], " KM Por litro")
print('----------------------------------------------------------------------------------------------')
print('==============================================================================================')


print(lista[0], " - ", lista[3][0], "L", " - ", round(km/lista[3][0], 2), "L",
      " - ", "O valor total em gasolina é de R$ {:.2f}".format(km/lista[3][0]*preco))
print('----------------------------------------------------------------------------------------------')
print(lista[1], " - ", lista[3][1], "L", " - ", round(km/lista[3][1], 2), "L",
      " - ", "O valor total em gasolina é de R$ {:.2f}".format(km/lista[3][1]*preco))
print('----------------------------------------------------------------------------------------------')
print(lista[2], " - ", lista[3][2], "L", " - ", round(km/lista[3][2], 2), "L",
      " - ", "O valor total em gasolina é de R$ {:.2f}".format(km/lista[3][2]*preco))
print('==============================================================================================')
