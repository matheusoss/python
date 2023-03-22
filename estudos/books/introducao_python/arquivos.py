'''
Programa 9.4 -> Gerando arquivos impares e pares com foco no estudo de Leitura e Escrita em arquivos externos txt, csv entre outros.

'''

# With em só uma linha

with open('impares.txt', 'w') as impares, open('pares.txt', 'w') as pares:
  for n in range(0, 1000):
    if n % 2 == 0:
      pares.write(f'{n}\n')
    else:
      impares.write(f'{n}\n')

  