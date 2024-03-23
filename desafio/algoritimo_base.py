import time
import requests
from colorama import Fore, Back, Style
import datetime

### TEMPO 30.533592 s

def request_test(hosts):
    
    for host in hosts:
        try:
            response = requests.get(host)
            if response.status_code == 200:
                print(Fore.GREEN + f'The host {host} is Ok.')
            else:
                print(Fore.RED + f'The host {host} is NOT Ok.') 
        except requests.RequestException :
            print(f'O site {host} não pôde ser alcançado')
            continue

ini = datetime.datetime.now()
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
total_time_requests = request_test(hosts)
end = datetime.datetime.now() - ini
print(Fore.YELLOW +"Tempo de execução (s):",  (end.total_seconds()) )
