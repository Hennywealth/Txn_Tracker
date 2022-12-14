from celery import shared_task
from time import sleep
from web3.auto import Web3
from .models import Address
import requests

bsc = "wss://ws-nd-256-341-637.p2pify.com/XXXXXXXXXXXXXXXXXXXXXXX"
# bsc = "wss://bsc.getblock.io/testnet/"
w3 = Web3(Web3.WebsocketProvider(bsc))



@shared_task(bind=True)
def log_loop(self, event_filter, poll_interval):
    global w3
    print(w3.isConnected())
    if event_filter == "block_filter":
        print(event_filter)
        event_filter = w3.eth.filter('pending')
    elif event_filter == 'tx_filter':
        print(event_filter)
        event_filter = w3.eth.filter('pending')
    else :
        pass
    
    while True:
        try:
            for event in event_filter.get_new_entries():
                txn = event.hex()
                data = w3.eth.getTransaction(txn)
                res = Address.objects.filter(address = data["to"])
                if len(list(res)) > 0: 
                    url = 'https://txntracker.herokuapp.com/'
                    my_obj = data["hash"]
                    my_obj =  data["hash"].hex()
                    requests.post(url, data = my_obj) 
                    print("Address found", data['to']) 
                else:
                    print('no address found')
        except Exception as e:
            print(e)
            log_loop(event_filter, poll_interval)
              
