import random, math, time, string
from math import sqrt, erfc
import matplotlib.pyplot as plt


# Convierte ese random de letras en binarios
def keychar_tobit(key):
    for i in range(len(key)):
        keychar="".join(str(key[i]))
    return "".join([bin(ord(letra))[2:].zfill(8) for letra in keychar])


# Comienza la prueba monobit
def monobit(bits):
    ceros = bits.count("0")
    unos = bits.count("1")
    frequencia = len(bits)
    SN = ceros - unos
    test = abs(SN) / sqrt(frequencia)
    return erfc(test / sqrt(2))


# main del programa
def pruebaMonobit(numeros):
    binfile = keychar_tobit(numeros)
    print(binfile)
    valor_p = monobit(binfile)
    if (valor_p < 0.01):
        print("Prueba de frecuencia Exitosa - Valor: "+ str(valor_p))
    else:
        print("Prueba de frecuencia No Exitosa - Valor: "+ str(valor_p))

