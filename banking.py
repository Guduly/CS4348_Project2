import threading

num_tellers = threading.Semaphore(0) 
num_customers = [threading.Semaphore(0) for _ in range(3)] 

readyCrit = threading.Semaphore(1)
readyTellers = []
serving = [None] * 3

def Teller(thread_id):
    print(f"Teller {thread_id} []: ready to serve")
    readyTellers.append(thread_id)
    num_tellers.release()
    num_customers.acquire()
    print(f"Teller {thread_id} []: waiting for a Customer")
    

def Customer(thread_id, action):
    print(f"Customer {thread_id} []: wants to perform {action} transaction")
    print(f"Customer {thread_id} []: Going to Bank")
    print(f"Customer {thread_id} []: Entering the Bank")
    print(f"Customer {thread_id} []: Getting to Line")
    print(f"Customer {thread_id} []: Selecting a Teller")

    num_tellers.acquire()
    if readyTellers:
        readyCrit.acquire()
        tid = readyTellers[0]
        readyCrit.release()
        readyTellers.pop(0)
        serving[tid] = thread_id
        print(f"Customer {thread_id} [Teller {tid}] []: Selects a Teller")
        print(f"Customer {thread_id} [Teller {tid}] [] Introduces itself")
        num_customers[tid].release() 

threads = []

for i in range(3): 
    threads.append(threading.Thread(target=Teller, args = (i,)))

for i in range(3): 
    threads.append(threading.Thread(target=Customer, args = (i,"Withdraw")))

for i in threads: 
    i.start()

for i in threads: 
    i.join()


