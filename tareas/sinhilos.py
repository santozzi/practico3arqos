import time
rango = 10000000
def tarea_1():
    print("Empezando tarea 1")
    
    for x in range(rango):
        pass
    
    print("Terminando tarea 1")
    
def tarea_2():
    print("Empezando tarea 2")
    time.sleep(1)
    print("Terminando tarea 2")
    
def tarea_3():
    print("Empezando tarea 3")
    time.sleep(4)
    print("Terminando tarea 3")

momento_arranque = time.perf_counter()
tarea_1()
tarea_2()
tarea_3()
momento_parada = time.perf_counter()

print(f"Tiempo transcurrido: {momento_parada - momento_arranque:0.5f} segundos")
