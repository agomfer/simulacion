# Generador Congruencial Lineal (GCL)
# Forma --> Xsub(n+1) = (a Xsub(n) + c) mod (m)

# Están determinados por los parámetros: * Módulo:  m > 0

# Multiplicador 0 <= a <= m
# Incremento c <= m
# Semilla 0 <= X sub0 <= m


def glc(seed, a, c, m, n):
    var = []
    rand = seed
    for i in range(n):
        rand = (a*rand + c) % m
        var.append(rand/m)
        result = '( ' + str(a) + ' * ' + str(rand) + ' + ' + str(c) + ' ) ' + ' % ' + str(m) + ' = ' + str(rand/m)
        print(result)
    return var



