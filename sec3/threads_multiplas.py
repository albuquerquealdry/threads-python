import threading
import time

def main():
    threads = [
        threading.Thread(target=contar, args=('jesus de skate', 10)),
        threading.Thread(target=contar, args=('massaru', 2)),
        threading.Thread(target=contar, args=('Comgu', 5)),
        threading.Thread(target=contar, args=('sac', 3))
    ]
    
    [th.start() for th in threads] 
    
    print("Fazendo outra coisa")
    print("teste" * 2)
    [th.join() for th in threads] 
    print("pronto")
    
def contar(oque, numero):
    for n in range(1, numero + 1):
        print(f'{n} {oque}(s)....')
        time.sleep(1)
        
if __name__ == "__main__" :
    main()