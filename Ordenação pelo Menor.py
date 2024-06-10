def buscaMenor(arr):
    menor = arr[0] 
    menor_indice = 0 
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr): 
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr) 
        novoArr.append(arr.pop(menor))
    return novoArr

lista = []
qnt_lista = int(input("Digite a quantidade á ser inserida na lista: "))
for i in range(qnt_lista):
    lista.append(int(input("Digite um número a ser inserido na lista: ")))

print("A lsita ordenada é: ",ordenacaoporSelecao(lista))