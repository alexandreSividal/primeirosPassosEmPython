# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cTlApreFlcRtY4ZhxHXi_SD885mTwYBo
"""

#numero descrescente
num1 = int(input('Informe o numero 1:'))
num2 = int(input('Informe o numero 2:'))
num3 = int(input('Informe o numero 3:'))

if (num1 >= num2) and (num1 >= num3):
  print(num1)
  if (num2 >= num3):
    print(num2)
    print(num3)
  else:
    print(num3)
    print(num2)
elif (num2 >= num1) and (num2 >= num3):
  print(num2)
  if (num3 >= num1):
    print(num3)
    print(num1)
  else:
    print(num1)
    print(num3)
else:
  print(num3)
  if (num1 >= num2):
    print(num1)
    print (num2)
  else:
    print(num2)
    print(num1)

#qual turno?
turno = input('Qual turno você estuda? Manhã, tarde ou noite?')

if (turno == 'manhã'):
  print ('Bom dia.')
elif (turno == 'tarde'):
  print ('Boa tarde.')
elif (turno == 'noite'):
  print ('Boa noite.')
else:
  print ('Valor invalido.')

#par ou impar?
numero = int(input('Digite um numero inteiro:'))

if numero % 2 == 0:
  print('O numero é par.')
else:
  print ('O numero é impar.')

#inteiro ou decimal?
numero = float(input('Digite um numero qualquer (pode ter casa decimal):'))

if numero % 1 == 0:
  print('O numero é inteiro.')
else:
  print ('O numero é decimal.')

num1 = float(input('Digite o numero 1:'))
num2 = float(input('Digite o numero 2:'))
operacao = input('Digite a operação que deseja +, -, *, /):')

#operações
if (operacao == '+'):
  resultado = num1+num2
  print (f'O resultado da operação é {resultado}')
elif (operacao == '-'):
  resultado = num1-num2
  print (f'O resultado da operação é {resultado}')
elif (operacao == '*'):
  resultado = num1*num2
  print (f'O resultado da operação é {resultado}')
elif (operacao == '/'):
  resultado = num1/num2
  print (f'O resultado da operação é {resultado}')
else:
  print ('Operação invalida, o resultado será zero.')
  resultado = 0

  #verificações
  #inteiro ou decimal?
if resultado % 1 == 0:
  print ('Resultado da operação é um numero inteiro.')
else:
  print ('Resultado da operação é um numero decimal.')

  #positivo ou negativo?
if resultado > 0:
  print ('Resultado da operação é um numero positivo.')
elif resultado < 0:
  print ('Resultado da operação é um numero negativo.')
else:
  print ('Resultado da operação é um numero neutro.')

  #par ou impar?
if resultado % 2 == 0:
  print ('Resultado da operação é um numero par.')
else:
  print ('Resultado da operação é um numero ímpar.')

#formando triangulo e classificando
print ('Vamos formar um triângulo?')

lado1 = float(input('Digite o tamanho do primeiro lado:'))
lado2 = float(input('Digite o tamanho do segundo lado:'))
lado3 = float(input('Digite o tamanho do terceiro lado:'))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2+lado3 > lado1):
  print ('Valores válidos para formar um triângulo.')
else:
  print ('Valores inválidos para formar um triângulo.')

if (lado1 == lado2) and (lado2 == lado3):
  print ('O triangulo é equilatero.')

if (lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
  print ('O triangulo é escaleno.')
else:
  print ('O triangulo é isosceles.')

#litro, tipo e desconto
valorLitroEtanol = 1.7
valorLitroDiesel = 2

qtdLitros = float(input('Digite q quantidade de combustivel abastecido:'))
tipo = input('Digite qual o tipo de combustivel abastecido (etanol ou diesel):')

if (tipo == 'etanol') and (qtdLitros <= 15):
  valorComDesconto = (valorLitroEtanol*0.98)*qtdLitros
  print (f'O valor abastecido em {tipo} ficou em: R${valorComDesconto}.')
elif (tipo == 'etanol') and (qtdLitros > 15):
  valorComDesconto = (valorLitroEtanol*0.96)*qtdLitros
  print (f'O valor abastecido em {tipo} ficou em: R${valorComDesconto}.')

elif (tipo == 'diesel') and (qtdLitros <= 15):
  valorComDesconto = (valorLitroDiesel*0.97)*qtdLitros
  print (f'O valor abastecido em {tipo} ficou em: R${valorComDesconto}.')
else:
  valorComDesconto = (valorLitroDiesel*0.95)*qtdLitros
  print (f'O valor abastecido em {tipo} ficou em: R${valorComDesconto}.')

#variacao percentual e sugestão de bonus
qtdVenda2022 = float(input('Digite a quantidade de vendas em R$ durante o ano de 2022:'))
qtdVenda2023 = float(input('Digite a quantidade de vendas em R$ durante o ano de 2023:'))
variacaoPercentual = ((qtdVenda2023-qtdVenda2022)/qtdVenda2022)*100

print (f'A variação percentual entre anos de 2023 e 2022 ficou em {variacaoPercentual}%.')

if variacaoPercentual >= 20:
  print ('Sugerimos bonificação para o time de vendas!')
elif (variacaoPercentual >= 2) and (variacaoPercentual < 20) :
  print ('Sugerimos uma pequena bonificação para o time e vendas.')
elif (variacaoPercentual >= -10) and (variacaoPercentual < 2):
  print ('Sugerimos planejamento e incentivo às vendas.')
else:
  print ('Sugerimos corte de gastos.')

