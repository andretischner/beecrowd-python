# Inicializando pasta
import sys

for linha in sys.stdin:
    a, b = map(int, linha.split())
    print(a ^ b)