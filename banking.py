import threading
import random 

num_tellers = threading.Semaphore(0) 
num_customers = [threading.Semaphore(0) for _ in range(3)] 

# Q & A 
customer_Res = [threading.Semaphore(0) for _ in range(3)]
teller_Ask = [threading.Semaphore(0) for _ in range(3)]
response = [None] * 3

readyCrit = threading.Semaphore(1)
readyTellers = []
serving = [None] * 3

def Teller(thread_id):
    print(f"Teller {thread_id} []: ready to serve")
    readyCrit.acquire()
    readyTellers.append(thread_id)
    readyCrit.release()

    num_tellers.release()
    print(f"Teller {thread_id} []: waiting for a Customer")
    num_customers[thread_id].acquire()
    
    print(f"Teller {thread_id} [Customer {serving[thread_id]}]: Serving a Customer")
    print(f"Teller {thread_id} [Customer {serving[thread_id]}]: Asks for Transaction")
    #num_customers[thread_id].release()

    teller_Ask[thread_id].release()
    customer_Res[thread_id].acquire();


def Customer(thread_id, action):
    print(f"Customer {thread_id} []: Wants to perform {action} transaction")
    print(f"Customer {thread_id} []: Going to Bank")
    print(f"Customer {thread_id} []: Entering the Bank")
    print(f"Customer {thread_id} []: Getting to Line")
    print(f"Customer {thread_id} []: Selecting a Teller")

    num_tellers.acquire()
    
    readyCrit.acquire()
    tid = readyTellers.pop(0) 
    readyCrit.release()
    
    serving[tid] = thread_id
    print(f"Customer {thread_id} [Teller {tid}]: Selects a Teller")
    print(f"Customer {thread_id} [Teller {tid}] Introduces itself")
    num_customers[tid].release() 

    teller_Ask[tid].acquire()
    response[tid] = action
    print(f"Customer {thread_id} [Teller {tid}]: Asks for a {action} transaction")
    customer_Res[tid].release()
    


    

threads = []

for i in range(3): 
    threads.append(threading.Thread(target=Teller, args = (i,)))

options = ["Deposit", "Withdrawal"]

for i in range(3): 
    threads.append(threading.Thread(target=Customer, args = (i,random.choice(options))))

for i in threads: 
    i.start()

for i in threads: 
    i.join()


