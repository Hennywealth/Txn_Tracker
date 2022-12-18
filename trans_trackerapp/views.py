from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Address
from.tasks import  log_loop

def test(request):
   
    log_loop.delay("block_filter", 0)
    if request.method == "POST":
        body_unicode = request.body	
        body = json.loads(body_unicode.decode('utf-8')) 
        name = body['name']
        address = body['address']
        new_data = Address(name=name, address=address)
        new_data.save()
        return HttpResponse('Done')
        
    return HttpResponse(' Json Post request format { "name" : "test16", "address":"0x89aB180B100D396d6FFCFCd468969E97799bB245"}')


# def handle_event(event):
#     print(event)

# async def log_loop(event_filter, poll_interval):
#     while True:
#         for event in event_filter.get_new_entries():
#             txn = event.hex()
#             data = w3.eth.getTransaction(txn)
#             res = Address.objects.filter(address = data["from"])
            
#             if len(list(res)) > 0:
#                 url = 'http://127.0.0.1:8000/'
#                 myobj = data["hash"]
                
#                 # requests.post(url, json = myobj)  
                
#             else:
#                 print('no address found')
            
#         await asyncio.sleep(poll_interval)
        

# def main():
#     block_filter = w3.eth.filter('pending')
#     tx_filter = w3.eth.filter('pending')
#     loop = asyncio.get_event_loop()
#     try:
#         loop.run_until_complete(
#             asyncio.gather(
#                 log_loop(block_filter, 2),
#                 log_loop(tx_filter, 2)))
#     finally:
#         loop.close()
    

# if __name__ == '__main__':
#     main()
    

           