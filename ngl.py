import random
import string
import requests
import os
from pystyle import Colors, Colorate
import time

def ngl():
    def deviceId():
        characters = string.ascii_lowercase + string.digits

        part1 = ''.join(random.choices(characters, k=8))
        part2 = ''.join(random.choices(characters, k=4))
        part3 = ''.join(random.choices(characters, k=4))
        part4 = ''.join(random.choices(characters, k=4))
        part5 = ''.join(random.choices(characters, k=12))

        device_id = f"{part1}-{part2}-{part3}-{part4}-{part5}"

        return device_id
    
    def UserAgent():
        with open('user-agents.txt', 'r') as file:
            user_agents = file.readlines()
            random_user_agent = random.choice(user_agents).strip()
            
            return random_user_agent
            
    def Proxy():
        with open('proxies.txt', 'r') as file:
            proxies_list = file.readlines()
            if not proxies_list:
                print(R + "[-]" + W + " Error: proxies.txt is empty. Please add proxies to the file.")
                exit(1)
            random_proxy = random.choice(proxies_list).strip()

        proxies = {
            'http': random_proxy,
            'https': random_proxy
        }
        return proxies
        
    R = '\033[31m'
    G = '\033[32m'
    W = '\033[0m'

    os.system('cls' if os.name == 'nt' else 'clear')


    print(Colorate.Vertical(Colors.blue_to_purple,"""
    
HELLO THIS IS CAMERGET
HELLO THIS IS CAMERGET
HELLO THIS IS CAMERGET
HELLO THIS IS CAMERGET
HELLO THIS IS CAMERGET
HELLO THIS IS CAMERGET
HELLO THIS IS CAMERGET
HELLO THIS IS CAMERGET
HELLO THIS IS CAMERGET
HELLO THIS IS CAMERGET
HELLO THIS IS CAMERGET    """))
    
    
    nglusername = input(Colorate.Vertical(Colors.blue_to_purple,"NICKNAME: "))
    message = input(Colorate.Vertical(Colors.blue_to_purple,"MESSAGE: "))
    Count = int(input(Colorate.Vertical(Colors.blue_to_purple,"COUNTS: ")))
    delay = float(input(Colorate.Vertical(Colors.blue_to_purple,"time send: ")))
    use_proxy = input(Colorate.Vertical(Colors.blue_to_purple, "USE PROXY (y/n): ")).lower()

    if use_proxy == "y":
        proxies = Proxy()
    else:
        proxies = None

    print(Colorate.Vertical(Colors.green_to_blue,"**********************************************************"))

    value = 0
    notsend = 0
    while value < Count:
        headers = {
            'Host': 'ngl.link',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': f'{UserAgent()}',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://ngl.link',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://ngl.link/{nglusername}',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
            'username': f'{nglusername}',
            'question': f'{message}',
            'deviceId': f'{deviceId()}',
            'gameSlug': '',
            'referrer': '',
        }

        try:
            response = requests.post('https://ngl.link/api/submit', headers=headers, data=data, proxies=proxies)
            if response.status_code == 200:
                notsend = 0
                value += 1
                print(G + "[+]" + W + "send spam 2#$$@$#$#$" + G + "{}".format(value) + W)
            else:
                notsend += 1
                print(R + "[-]" + W + "Fuck! not sended")
            if notsend == 4:
                print(R + "[!]" + W + "stop! im check info M#")
                deviceId()
                UserAgent()
                if use_proxy == "y":
                    proxies = Proxy()
                notsend = 0

            time.sleep(delay)  

        except requests.exceptions.ProxyError as e:
            print(R + "[-]" + W + "proxy not work" + W)
            if use_proxy == "y":
                proxies = Proxy()

ngl()
