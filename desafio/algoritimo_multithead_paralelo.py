import time
import datetime
import requests
from colorama import Fore
import threading
import multiprocessing
import random

def thread_orq(objects_number_in_list, host_list):
    core_quantitity = multiprocessing.cpu_count()
    if objects_number_in_list < core_quantitity:
        core_quantitity = objects_number_in_list
    threads = []
    for n in range(1, core_quantitity + 1):
        thread_ind = random.randint(1, 100)
        ini   = round(objects_number_in_list * (n - 1) / core_quantitity)
        end   = round(objects_number_in_list * n / core_quantitity)
        print (f"Core {n} processando de {ini} ate {end} Thread {thread_ind}")
        threads.append(
            threading.Thread(target=request_test, args=(host_list, ini, end, thread_ind, ), daemon=True, name=thread_ind)
        )
    [th.start() for th in threads]
    [th.join() for th in threads]

def request_test(hosts, start_index, end_index, thread_ind):
    for host in hosts[start_index:end_index]:
        try:
            response = requests.get(host)
            if response.status_code == 200:
                print(Fore.GREEN + f'[THREAD: {thread_ind}] The host {host} is Ok.')
            else:
                print(Fore.RED + f'[THREAD: {thread_ind}] The host {host} is NOT Ok.') 
        except requests.RequestException :
            print(f'[THREAD: {thread_ind}] Host {host} not found')
            continue


hosts = [
    "https://wikipedia.org",
    "https://youtube.com",
    "https://facebook.com",
    "https://amazon.com",
    "https://netflix.com",
    "https://twitter.com",
    "https://instagram.com",
    "https://reddit.com",
    "https://apple.com",
    "https://microsoft.com",
    "https://bbc.co.uk",
    "https://cnn.com",
    "https://nytimes.com",
    "https://ebay.com",
    "https://aliexpress.com",
    "https://coursera.org",
]
ini = datetime.datetime.now()
thread_orq(len(hosts), hosts)
end = datetime.datetime.now() - ini
print(Fore.YELLOW +"Tempo de execução (s):",  (end.total_seconds()) )
