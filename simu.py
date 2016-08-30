
# -*- coding: utf-8 -*-
import simpy
import random
import math
'''
Autores:
Carlos Calderon, 15219
Jorge Azmitia,15202
29 de Agosto del 2016
Modulo que simula un sistema operativo
'''

def proceso(env, name, cpu,llegada, tiempo,velocidad):
    global tiempoTotal
    yield env.timeout(llegada) #Llegada de procesos
    tiempollegada = env.now #registrar la llegada 
    # new
    asignarRam = random.randint(1,10)
    with ram.get(asignarRam) as req:  #Solicitud de proceso nuevo
        yield req
        yield env.timeout(tiempo)

    #ready
    instrucciones = random.randint(1,10)
    while instrucciones > 0:      #Mientras haya instrucciones, se van haciendo de 3 en 3 o 6 en 6
    #running
      with cpu.request() as req:  #Conectarse al cpu
          yield req
          yield env.timeout(tiempo)
          instrucciones = instrucciones - velocidad
          # Salida
      entraOS = random.randint(1,2)
      if entraOS == 1:  #Si es 1 pasa a la cola
        with os.request() as req:
          yield req
          yield env.timeout(1) #terminated

    ram.put(asignarRam) 
    
    tiempoUso = env.now - tiempollegada
    control.append(tiempoUso)
    tiempoTotal = tiempoTotal + tiempoUso    

# Ejecutar programa 
env = simpy.Environment()  #crear ambiente de simulacion
memoriaRam = 100 #cantidad de memoria ram
cpu = simpy.Resource(env, capacity=1) #cpu
ram = simpy.Container(env, init=memoriaRam, capacity=memoriaRam) #capacidad de memoria es 100
os = simpy.Resource(env, capacity=1) 
tiempoTotal = 0.0   #tiempo de todos los procesos
noprocesos = 100 #numero de procesos
RANDOM_SEED = 42 #Semilla
random.seed(RANDOM_SEED)
interval = 10 #Intervalo
velocidad = 3 #Velocidad
control=[] #Lista para tener lso tiempos
# crear los procesos
for i in range(noprocesos):
    t = random.expovariate(1.0 / interval)
    env.process(proceso(env, 'Proceso %d' % i, cpu, t, 1,3))
# correr la simulacion
env.run()


#calcular promedio y desviacion
aux=0
promedio=0
promedio = tiempoTotal/noprocesos
for i in range(noprocesos):
    aux += (promedio-control[i])*(promedio-control[i])
des = math.sqrt(aux/noprocesos)
#Desplegar calculos
print ('La desviacion estandar es %f' %des)
print ('En promedio se tardan %d' %promedio)
print ('Tiempo total %d' %tiempoTotal)
