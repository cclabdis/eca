x = input('Palavra 1: ')
y = input('Palavra 2:')

if len(x) != len(y):
  print('palavras sao diferentes')
  exit()
else:
  aux = 0
  for i in range(len(x)):
    if x[i] != y[i]:
      print('e palavras sao diferentes')
      aux = 1
      break
  if aux == 0:
    print('as palavras sao iguais')
