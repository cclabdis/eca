def alimentaarray():
  array = []
  aux = "oi" 
  while aux != "fim":
    aux = input('valores: ')
    if aux != 00:
      if aux.isdigit():
        array.append(int(aux))
    else : 
      break
  return array

def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array

def busca_binaria(a, item):
    esquerda = 0
    direita = len(a) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if a[meio] == item:
            return meio
        elif a[meio] > item:
            direita = meio - 1
        else: # a[meio] < item
            esquerda = meio + 1
    return -1



data = alimentaarray()
data = insertionSort(data)
print('Sorted Array in Asc Order:')
print(data)

y = input('entre com o numero a ser encontrado: ')
print("Localizacao:", busca_binaria(data, int(y)))
