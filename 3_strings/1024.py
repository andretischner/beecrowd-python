# Inicializando pasta
n = int(input())

for _ in range(n):
    texto = input()
    
    # Primeira passada: desloca letras 3 posições para direita
    primeira = ""
    for char in texto:
        if char.isalpha():
            primeira += chr(ord(char) + 3)
        else:
            primeira += char
    
    # Segunda passada: inverte a string
    segunda = primeira[::-1]
    
    # Terceira passada: desloca caracteres da metade em diante 1 posição para esquerda
    tamanho = len(segunda)
    metade = tamanho // 2
    
    terceira = ""
    for i in range(tamanho):
        if i >= metade:
            terceira += chr(ord(segunda[i]) - 1)
        else:
            terceira += segunda[i]
    
    print(terceira)