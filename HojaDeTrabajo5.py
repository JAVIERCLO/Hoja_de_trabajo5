import simpy as sp #Para hacer las simulaciones
import random #Para generar los números aleatorios
import matplotlib as mpl #Para hacer las gráficas

RANDOM_SEED = 42

RAM = sp.Container(env, init=100, capacity=100)

NProcesos = 25 #Número de procesos para simular
Instrucciones_ejecutables = 3 #instrucciones simultaneas que el CPU puede ejecutar
RAM_necesaria = random(1,10)
Instrucciones_proceso = random(1,10) #Número de instrucciones que tiene cada proceso
Tiempo = 10 #Tiempo que tarda el CPU en ejecutar el número definido de instrucciones


