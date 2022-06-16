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


data = alimentaarray()
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)
