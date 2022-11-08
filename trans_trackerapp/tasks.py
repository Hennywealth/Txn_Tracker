from celery import shared_task
from time import sleep
from web3.auto import Web3
from .models import Address
import requests

bsc = "wss://ws-nd-256-341-637.p2pify.com/0ebd6247159bb3dca20ed01a839a3551"
# bsc = "wss://bsc.getblock.io/testnet/"
w3 = Web3(Web3.WebsocketProvider(bsc))


@shared_task(bind=True)
def log_loop(self,  event_filter, poll_interval):
    global w3
    
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
                    # url = 'http://127.0.0.1:8000/'
                    my_obj = data["hash"]
                    # requests.post(url, json = my_obj)
                    # password = data["hash"].hex()
                
                    print("Address found", data['to'])
                    
                    print(my_obj)

                else:
                    print('no address found')
        except Exception as e:
            print(e)
            log_loop(event_filter, poll_interval)
              
