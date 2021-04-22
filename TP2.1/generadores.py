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



# Generador Método de los cuadrados medios
# Forma --> Usub(1) = Xsub(1) / 10^4

def cuadradosmedios(seed,n):
    seeds= []
    seeds.append(seed)
    values= []
    for i in range(n):
        v = seeds[i]**2
        values.append(v)
        x = int(str(v).zfill(8)[2:6])
        seeds.append(x)
        print('seed: ' + str(seeds[i]) + ' - Value: ' + str(values[i]))
    return seeds, values





