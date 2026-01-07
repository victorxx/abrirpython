A=int(input("primeiro termo"))
B=int(input("SEGUNDO TERMO"))
if abs(A)>1000 or abs(B)>1000:
    print('ok deu algo errado')
    print('você digitou valor negativo ou a cima de 1000')
    
else:
    soma=A+B
    print(soma)
    print('resultado da soma a cima')
