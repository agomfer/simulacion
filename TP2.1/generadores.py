# Generador Congruencial Lineal (GCL)
# Forma --> Xsub(n+1) = (a Xsub(n) + c) mod (m)

# Están determinados por los parámetros: * Módulo:  m > 0

# Multiplicador 0 <= a <= m
# Incremento c <= m
# Semilla 0 <= X sub0 <= m


valores = []


def glc(r, a, c, m, n):
    var = []
    rand = r
    for i in range(n):
        rand = (a*rand + c) % m
        var.append(rand/m)
        result = '( ' + str(a) + ' * ' + str(rand) + ' + ' + str(c) + ' ) ' + ' % ' + str(m) + ' = ' + str(rand/m)
        print(result)
    return var


a = 25214903917
c = 11
m = 2**48

valores=glc(2,a,c,m,10)

