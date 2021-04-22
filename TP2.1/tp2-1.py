# Generador Congruencial Lineal (GCL)
# Forma --> Xsub(n+1) = (a Xsub(n) + c) mod (m)

# Están determinados por los parámetros: * Módulo:  m > 0

# Multiplicador 0 <= a <= m
# Incremento c <= m
# Semilla 0 <= X sub0 <= m


valores = [];

def seedLCG(initVal):
    global rand
    rand = initVal

def lcg(a, c, m, n):
    var = []
    global rand
    for i in range(n):
        rand = (a*rand + c) % m
        var.append(rand)
        result = '( ' + str(a) + ' * ' + str(rand) + ' + ' + str(c) + ' ) ' + ' % ' + str(m) + ' = ' + str(rand)
        print(result)
    return var


a = 25214903917
c = 11
m = 2**48

seedLCG(2)
valores=lcg(a,c,m,10)

