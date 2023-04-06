from btc import __private_to_compressed_public
from btc import generate_address_btc
from eth import generate_address
from ltc import to_wallet
from doge import dogeaddress
from checker import balances
import generator
import os
import requests
import time
#import ctypes

def main():
    private_key = generator.gnr.KeyGenerator()
    mnemonick = generator.gnr.seed_generator()
    pubkey = str(__private_to_compressed_public(private_key))
    address_btc = generate_address_btc(private_key)
    address_eth = generate_address(private_key)
    address_ltc = to_wallet(pubkey)
    address_doge = dogeaddress(pubkey)
    address = address_btc
    btc_bal = balances(address)
    address = address_eth
    eth_bal = balances(address)
    address = address_ltc
    ltc_bal = balances(address)
    address = address_doge
    doge_bal = balances(address)
    try:
        if float(btc_bal+eth_bal+ltc_bal+doge_bal) > 0:
            with open('wallet.list', "a")as list:
                list.write(f'====================================================================================================================\nmnemonick : {mnemonick}\nbtc private key : {private_key}\npublick key : {pubkey}\naddress btc : {address_btc}\nbtc balance : {btc_bal}\naddress eth : {address_eth}\neth balance : {eth_bal}\naddress_ltc : {address_ltc}\nltc balance : {ltc_bal}\naddress doge : {address_doge}\ndoge balance : {doge_bal}') #save all data in file
        print(f'=====================================================================================================================\nmnemonick : {mnemonick}\n\naddress btc : {address_btc}\nbtc balance : {btc_bal}\naddress eth : {address_eth}\neth balance : {eth_bal}\naddress_ltc : {address_ltc}\nltc balance : {ltc_bal}\naddress doge : {address_doge}\ndoge balance : {doge_bal}\n\n=====================================================================================================================') #print information
    except:
        print(f'=====================================================================================================================\nmnemonick : {mnemonick}\n\naddress btc : {address_btc}\nbtc balance : {btc_bal}\naddress eth : {address_eth}\neth balance : {eth_bal}\naddress_ltc : {address_ltc}\nltc balance : {ltc_bal}\naddress doge : {address_doge}\ndoge balance : {doge_bal}\n\n=====================================================================================================================') #print information
    main()


def isInternet():
    global internet
    try:
            try:
                requests.get("http://1.1.1.1")
            except :
                requests.get("http://1.0.0.1")
            internet = True
    except :
            internet = False


def bonjour ():
    global threads
    #ctypes.windll.kernel32.SetConsoleTitleW("BTC | ETH | LTC | DOGE | Software @destroycorp v1.0 | ")
    try:
        threads = int(input("select the number of threads for the script to run(only in numbers): "))
        print("okay,get started")
        time.sleep(1)
        if not os.path.exists('wallet.list'):
            with open('wallet.list', "w+")as x:
                print('file wallet.list not found, but I created him') #create log files
        time.sleep(2.5)
    except:
        print("fatal error!!! \n please rerun script and input correct number")
        import sys
        sys.exit(0)
    if threads == 0:
        threads = 10
    while True:
        isInternet ()
        if not internet:
            print("no internet")
            time.sleep(0.5)
        else:
            break
    from threading import Thread
    for _ in range (threads):
        th = Thread(target=main, args=())#added script to threads
        th.start()
bonjour () #bonjour)
