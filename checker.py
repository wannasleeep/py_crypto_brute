import requests
from bs4 import BeautifulSoup

def balances_btc(address_btc):
    try:
        try:
            try:
                url = f"https://chain.so/api/v2/get_address_balance/BTC/{address_btc}"
                response = requests.get(url, proxies = {
                    'http': get_proxy()}).json()
                return response['data']['confirmed_balance']
            except:
                url = f"https://chain.so/api/v2/get_address_balance/BTC/{address_btc}"
                response = requests.get(url, proxies = {
                    'http': txt_proxy()}).json()
                return response['data']['confirmed_balance']
        except:
            try:
                url = f"https://api-r.bitcoinchain.com/v1/address/{address_btc}"
                response = requests.get(url, proxies = {
                    'http': get_proxy()}).json()
                return response['0']['balance']
            except:
                url = f"https://api-r.bitcoinchain.com/v1/address/{address_btc}"
                response = requests.get(url, proxies = {
                    'http': txt_proxy()}).json()
                return response['0']['balance']
    except:
        try:
            url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address_btc}"
            response = requests.get(url, proxies = {
                'http': get_proxy()}).json()
            return response['balance']
        except:
            url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address_btc}"
            response = requests.get(url, proxies = {
                'http': txt_proxy()}).json()
            return response['balance']


def balances_eth(address_eth):
    try:
        try:
            try:
                url = f"https://api.blockcypher.com/v1/eth/main/addrs/{address_eth}"
                response = requests.get(url, proxies = {
                    'http': get_proxy()}).json()
                return response['balance']
            except:
                url = f"https://api.blockcypher.com/v1/eth/main/addrs/{address_eth}"
                response = requests.get(url, proxies = {
                    'http': txt_proxy()}).json()
                return response['balance']
        except:
            try:
                url = f"https://web3api.io/api/v1/addresses/{address_eth}"
                response = requests.get(url, proxies = {
                    'http': get_proxy()}).json()
                return response['balance']
            except:
                url = f"https://web3api.io/api/v1/addresses/{address_eth}"
                response = requests.get(url, proxies = {
                    'http': txt_proxy()}).json()
                return response['balance']
    except:
        try:
            url = f"http://api.ethplorer.io/getAddressInfo/{address_eth}?apiKey=freekey"
            response = requests.get(url, proxies = {
                'http': get_proxy()}).json()
            return response['ETH']['balance']
        except:
            url = f"http://api.ethplorer.io/getAddressInfo/{address_eth}?apiKey=freekey"
            response = requests.get(url, proxies = {
                'http': txt_proxy()}).json()
            return response['ETH']['balance']

def balances_ltc(address_ltc):
        try:
            try:
                try:
                    url = f"https://chain.so/api/v2/get_address_balance/LTC/{address_ltc}"
                    response = requests.get(url, proxies = {
                        'http': get_proxy()}).json()
                    return response['data']['confirmed_balance']
                except:
                    url = f"https://chain.so/api/v2/get_address_balance/LTC/{address_ltc}"
                    response = requests.get(url, proxies = {
                        'http': txt_proxy()}).json()
                    return response['data']['confirmed_balance']
            except:
                try:
                    url = f"https://chain.api.btc.com/v3/address/{address_ltc}"
                    response = requests.get(url, proxies = {
                        'http': get_proxy()}).json()
                    return response['balance']
                except:
                    url = f"https://chain.api.btc.com/v3/address/{address_ltc}"
                    response = requests.get(url, proxies = {
                        'http': txt_proxy()}).json()
                    return response['balance']
        except:
            try:
                url = f"https://api.blockcypher.com/v1/ltc/main/addrs/{address_ltc}"
                response = requests.get(url, proxies = {
                    'http': get_proxy()}).json()
                return response['balance']
            except:
                url = f"https://api.blockcypher.com/v1/ltc/main/addrs/{address_ltc}"
                response = requests.get(url, proxies = {
                    'http': txt_proxy()}).json()
                return response['balance']


def balances_doge(address_doge):
        try:
            try:
                try:
                    url = f"https://chain.so/api/v2/get_address_balance/DOGE/{address_doge}"
                    response = requests.get(url, proxies = {'http': get_proxy()}).json()
                    return response['data']['confirmed_balance']
                except:
                    url = f"https://chain.so/api/v2/get_address_balance/DOGE/{address_doge}"
                    response = requests.get(url, proxies = {'http': txt_proxy()}).json()
                    return response['data']['confirmed_balance']
            except:
                try:
                    url = f"https://dogechain.info/api/v1/address/balance/{address_doge}"
                    response = requests.get(url, proxies = {'http': get_proxy()}).json()
                    return response['balance']
                except:
                    url = f"https://dogechain.info/api/v1/address/balance/{address_doge}"
                    response = requests.get(url, proxies = {'http': txt_proxy()}).json()
                    return response['balance']
        except:
            try:
                url = f"https://api.blockcypher.com/v1/doge/main/addrs/{address_doge}"
                response = requests.get(url, proxies = {'http': get_proxy()}).json()
                return response['balance']
            except:
                url = f"https://api.blockcypher.com/v1/doge/main/addrs/{address_doge}"
                response = requests.get(url, proxies = {'http': txt_proxy()}).json()
                return response['balance']

#s etim nado choto delat ibo eto kostily ebuchiy
n = 0
m = 0
def get_proxy():
    global n
    try:
        n += 1
        a = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
        f = a.text
        soup = BeautifulSoup(f, 'html.parser')
        l = [line.strip() for line in soup]
        return l[n]
    except:
        n = 0
        n += 1
        a = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
        f = a.text
        soup = BeautifulSoup(f, 'html.parser')
        l = [line.strip() for line in f]
        return l[n]

def txt_proxy():
    try:
        m += 1
        with open('proxy.txt', "r")as list:
            l = [line.strip() for line in list]
            return l[m]
    except:
        m = 0
        m += 1
        with open('proxy.txt', "r")as list:
            l = [line.strip() for line in list]
            return l[m]
