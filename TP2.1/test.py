import random, math, time, string
from math import sqrt, erfc
import matplotlib.pyplot as plt
from scipy import stats


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


# Estadistica descriptiva 
def EstDesc(datos,vals):
    vals = stats.describe(datos)
    #valores.append(vals)

    freqs = stats.relfreq(datos,100)
    #valores.append(freqs)

    print ("Estadistica descriptiva: \n")
    print (vals)
    print ("\nFrecuencias relativas: \n")
    print (freqs)
    freqrel = freqs[0]
    return freqrel

# Prueba Chi Cuadrado con la biblioteca SciPy.stats
def ChiCuad(freqs):

    esperados = []
    for i in range(100):
        esperados.append(0.01)

    chiCuad = stats.chisquare(freqs,esperados,0,0)
    
    print ("\nPrueba Chi Cuadrado\n")
    print(chiCuad)
    print ("\n\n")
    
    
    #valores.append(chiCuad)
    
    