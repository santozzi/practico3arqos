import time
import threading 

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
thr1 = threading.Thread(target=tarea_1)
thr2 = threading.Thread(target=tarea_2)
thr3 = threading.Thread(target=tarea_3)
thr1.start()
thr2.start()
thr3.start()

thr1.join()
thr2.join()
thr3.join()

momento_parada = time.perf_counter()

print(f"Tiempo transcurrido: {momento_parada - momento_arranque:0.5f} segundos")
