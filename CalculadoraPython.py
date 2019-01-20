# Título do programa
print("\n******************* Python Calculator *******************")

#Pula uma linha e imprime na tela
print("\nSelecione o número da operação desejada:") 

# Pula uma linha e oferece as opções de cálculo
print("\n1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão") # imprime na tela

# Pula uma linha e mostra para o  usuário a opção de cálculo desejada
option = int(input("\nDigite sua opção (1/2/3/4): "))

# Entrada do primeiro número e pula uma linha
firstNumber = int(input("\nDigite o primeiro número: "))
# Entrada do segundo número
secondNumber = int(input("Digite o segundo número: "))

#Cálculo de soma
if option == 1: 
	soma = firstNumber + secondNumber
	print(firstNumber, "+",secondNumber, "=", soma)
# Cálculo de subtração
elif option == 2:
	subtraction = firstNumber - secondNumber
	print(firstNumber, "-", secondNumber, "=", subtraction)
# Cálculo de multiplicação
elif option == 3:
	multiply = firstNumber * secondNumber
	print(firstNumber, "*", secondNumber, "=", multiply)
# Cálculo de divisão
elif option == 4:
	division = firstNumber / secondNumber
	print(firstNumber, "/", secondNumber, "=", division)
else:
	print("Opção inválida!")








