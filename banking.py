import threading

num_tellers = threading.Semaphore(0) 
num_customers = threading.Semaphore(0) 

waiting = []
ready = []
serving = [None] * 3

def Teller(thread_id):
    print(f"Teller {thread_id} []: ready to serve")
    ready.append(thread_id)
    num_tellers.release()
    num_customers.acquire()
    print(f"Teller {thread_id} []: waiting for a Customer")
    

def Customer(thread_id, action):
    print(f"Customer {thread_id} []: waiting to perform {action} transaction")
    num_tellers.acquire()
    num_customers.release() 

    print(f"Customer {thread_id} []: Going to Bank")
    print(f"Customer {thread_id} []: Entering the Bank")
    print(f"Customer {thread_id} []: Getting to Line")
    print(f"Customer {thread_id} []: Selecting a Teller")

    if ready:
        if waiting:
            tid = ready[0]
            ready.pop(0)
            serving[tid] = waiting[0]
            waiting.pop(0)
            print(f"Customer {thread_id} [Teller {tid}] []: Selects a Teller")
            print(f"Customer {thread_id} [Teller {tid}] [] Introduces itself")
            num_tellers.acquire()
        else: 
            tid = ready[0]
            ready.pop(0)
            serving[tid] = thread_id
            print(f"Customer {thread_id} [Teller {tid}] []: Selects a Teller")
            print(f"Customer {thread_id} [Teller {tid}] [] Introduces itself")
            num_tellers.acquire()
    else: 
        waiting.append(thread_id)


threads = []

for i in range(3): 
    threads.append(threading.Thread(target=Teller, args = (i,)))

for i in range(3): 
    threads.append(threading.Thread(target=Customer, args = (i,"Withdraw")))

for i in threads: 
    i.start()

for i in threads: 
    i.join()


