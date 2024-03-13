import threading

def funcabc(param):
    print("executando...")
    print(f"Executado recebendo: {param}")


th1 =  threading.Thread(target=funcabc, args=("Thread 1",))
th2 =  threading.Thread(target=funcabc, args=("Thread 2",))

while True:
    th2.start()
    th2.join()

    th1.start()
    th1.join()
