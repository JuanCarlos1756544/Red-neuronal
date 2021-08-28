def pesos():  # pesos red random 

    random.seed(7) 

    capa_oculta = [[rand(-100, 100) / 100 for _ in range(tamano_entrada + 1)] 

                   for _ in range(numero_ocultas)] 

    capa_salida = [[rand(-100, 100) / 100 for _ in range(numero_ocultas + 1)] 

                   for _ in range(tamalo_salida)] 

    return capa_oculta, capa_salida 

def prediccion(numero): 

    return ffnn(red_neuronal,entradas[numero])[-1] 

objetivo = [[1 if i == j else 0 for i in range(10)] for j in range(10)] 

tamano_entrada = 25 

numero_ocultas = 5 

tamalo_salida = 10 

rand = partial(random.randint) 

capa_oculta, capa_salida = pesos() 

red_neuronal = [capa_oculta, capa_salida] 

print(red_neuronal) 

 

promedio_errores_cuadrados = 1 

i = 1 

while promedio_errores_cuadrados > 0.005: 

    oculta, saida, error1 = backpropagation(red_neuronal, entradas[0], objetivo[0]) 

    red_neuronal = [oculta, saida] 

    oculta, saida, error2 = backpropagation(red_neuronal, entradas[1], objetivo[1]) 

    red_neuronal = [oculta, saida] 

    oculta, saida, error3 = backpropagation(red_neuronal,entradas[2], objetivo[2]) 

    red_neuronal = [oculta, saida] 

    oculta, saida, error4 = backpropagation(red_neuronal, entradas[3], objetivo[3]) 

    red_neuronal = [oculta, saida] 

    oculta, saida, error5 = backpropagation(red_neuronal, entradas[4], objetivo[4]) 

    red_neuronal = [oculta, saida] 

    oculta, saida, error6 = backpropagation(red_neuronal, entradas[5], objetivo[5]) 

    red_neuronal = [oculta, saida] 

    oculta, saida, error7 = backpropagation(red_neuronal, entradas[6], objetivo[6]) 

    red_neuronal = [oculta, saida] 

    oculta, saida, error8 = backpropagation(red_neuronal,entradas[7], objetivo[7]) 

    red_neuronal = [oculta, saida] 

    oculta, saida, error9 = backpropagation(red_neuronal, entradas[8], objetivo[8]) 

    red_neuronal = [oculta, saida] 

    oculta, saida, error10 = backpropagation(red_neuronal, entradas[9], objetivo[9]) 

    red_neuronal = [oculta, saida] 

    promedio_errores_cuadrados = (error1 + error2 + error3 + error4 + error5 + error6 + error7 + error8 + error9 + error10) / 10 

    print("promedio errores cuadrados:", promedio_errores_cuadrados) 

    print("iterracion:", i) 

    i = i + 1 

print(red_neuronal) 

print(prediccion(0)) 

print(imprimr(entradas[0])) 

print(prediccion(1)) 

print(imprimr(entradas[1])) 

print(prediccion(2)) 

print(imprimr(entradas[2])) 

print(prediccion(3)) 

print(imprimr(entradas[3])) 

print(prediccion(4)) 

print(imprimr(entradas[4])) 

print(prediccion(5)) 

print(imprimr(entradas[5])) 

print(prediccion(6)) 

print(imprimr(entradas[6])) 

print(prediccion(7)) 

print(imprimr(entradas[7])) 

print(prediccion(8)) 

print(imprimr(entradas[8])) 

print(prediccion(9)) 

print(imprimr(entradas[9])) 

 