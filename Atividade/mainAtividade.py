import math

a = int(input("informe o valor de a: "))
b = int(input("informe o valor de b: "))
c = int(input("informe o valor de c: "))

if a>b>c:
    print("O maior número é: ",a, "O menor número é: ", c)

if b>c>a:
    print("O maior número é: ", b, "O menor número é: ", a)

if c>a>b:
    print("O maior número é: ", c, "O menor número é: ", b)

