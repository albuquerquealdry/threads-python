import threading
import time

def main():
    th =  threading.Thread(target=contar, args=('jesus de skate', 10))
    
    th.start()
    
    print("Fazendo outra coisa")
    print("teste" * 2)
    th.join()
    print("pronto")
    
def contar(oque, numero):
    for n in range(1, numero + 1):
        print(f'{n} {oque}(s)....')
        time.sleep(1)
        
if __name__ == "__main__" :
    main()