import threading

num_tellers = threading.Semaphore(0) 
num_customers = threading.Semaphore(0) 

def Teller(thread_id):
    print(f"Teller {thread_id} []: ready to serve")
    num_tellers.release()
    num_customers.acquire()

def Customer(thread_id, action):
    print(f"Customer {thread_id} []: waiting to perform {action} transaction")
    num_tellers.acquire()
    num_customers.release() 

threads = []

for i in range(3): 
    threads.append(threading.Thread(target=Teller, args = (i,)))

for i in range(3): 
    threads.append(threading.Thread(target=Customer, args = (i,"Withdraw")))

for i in threads: 
    i.start()

for i in threads: 
    i.join()


