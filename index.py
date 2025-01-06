nome= str(input("Qual seu nome?"))
idade= int(input ("Qual sua idade?"))
print(f"Olá {nome}! Wow! Seus {idade} anos formam algo especial!")

n1= float(input("Digite um número:"))
n2= float(input("Digite outro número:"))
print("A soma dos números é", n1+n2)
if n1>n2:
    print("A diferença dos números é", n1-n2)
else:
    print("A diferença dos números é", n2-n1)
print("O produto dos números é", n1*n2)