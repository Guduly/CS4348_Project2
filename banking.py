import threading
import random, time  

num_tellers = threading.Semaphore(0) 
num_customers = [threading.Semaphore(0) for _ in range(3)] 

# Q & A 
customer_Res = [threading.Semaphore(0) for _ in range(3)]
teller_Ask = [threading.Semaphore(0) for _ in range(3)]
response = [None] * 3

readyCrit = threading.Semaphore(1)
readyTellers = []
serving = [None] * 3

# Customer Door 
door = threading.Semaphore(2)

# Manager permission 
manager = threading.Semaphore(1)

# safe entrance 
safe = threading.Semaphore(2)

# Teller Task Completion
teller_done = [threading.Semaphore(0) for _ in range(3)]
customer_done = [threading.Semaphore(0) for _ in range(3)]

# bank status
open = threading.Semaphore(0)
close = False

def Teller(thread_id):

    while True:
        open.release() 

        print(f"Teller {thread_id} []: ready to serve")
        readyCrit.acquire()
        readyTellers.append(thread_id)
        readyCrit.release()

        num_tellers.release()
        print(f"Teller {thread_id} []: waiting for a Customer")
        num_customers[thread_id].acquire()

        if close: 
            break
        
        print(f"Teller {thread_id} [Customer {serving[thread_id]}]: Serving a Customer")
        print(f"Teller {thread_id} [Customer {serving[thread_id]}]: Asks for Transaction")
        #num_customers[thread_id].release()

        teller_Ask[thread_id].release()
        customer_Res[thread_id].acquire();
        print(f"Teller {thread_id} [Customer {serving[thread_id]}]: Handling {response[thread_id]} transaction")

        if(response[thread_id] == "Withdrawal"):
            # manager wait time
            print(f"Teller {thread_id} [Customer {serving[thread_id]}]: Going to Manager")
            manager.acquire()
            print(f"Teller {thread_id} [Customer {serving[thread_id]}]: Talking with Manager")
            time.sleep(random.uniform(5, 30) / 1000)
            manager.release()
            print(f"Teller {thread_id} [Customer {serving[thread_id]}]: Received Manger Permission")
        
        print(f"Teller {thread_id} [Customer {serving[thread_id]}]: Going to Safe")
        
        safe.acquire()
        print(f"Teller {thread_id} [Customer {serving[thread_id]}]: Entering Safe")
        time.sleep(random.uniform(10, 50) / 1000) 
        print(f"Teller {thread_id} [Customer {serving[thread_id]}]: Leaving Safe")
        safe.release()

        print(f"Teller {thread_id} [Customer {serving[thread_id]}]: Finishing {response[thread_id]} transaction")
        print(f"Teller {thread_id} [Customer {serving[thread_id]}]: Wait for customer to leave")
        
        teller_done[thread_id].release()
        customer_done[thread_id].acquire()
    
    
    print(f"Teller {thread_id} []: Leaving for the day")





def Customer(thread_id, action):
    print(f"Customer {thread_id} []: Wants to perform {action} transaction")
    print(f"Customer {thread_id} []: Going to Bank")

    time.sleep(random.uniform(0, 100) / 1000)
    print(f"Customer {thread_id} []: Arrived at Bank")
    
    door.acquire()
    print(f"Customer {thread_id} []: Entering the Bank")
    door.release() 

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

    teller_done[tid].acquire()
    print(f"Customer {thread_id} [Teller {tid}]: Leaves Teller")
    customer_done[tid].release()

    door.acquire()
    print(f"Customer {thread_id} []: Goes to Door")
    door.release() 
    
    print(f"Customer {thread_id} []: Leaves Bank")
    


threads = []

for i in range(3): 
    threads.append(threading.Thread(target=Teller, args = (i,)))
    threads[i].start()

for _ in range(3): 
    open.acquire()

options = ["Deposit", "Withdrawal"]

for i in range(20): 
    threads.append(threading.Thread(target=Customer, args = (i,random.choice(options))))



for i in threads[3:]: 
    i.start()

for i in threads[3:]: 
    i.join()

close = True

for i in threads[:3]: 
    i.join()

print("The bank closes for today")


