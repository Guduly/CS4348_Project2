import threading

num_tellers = threading.Semaphor(0) 
num_customers = threading.Semaphor(0) 

def Teller(thread_id):
    print(f"Teller {thread_id} []: ready to serve")
    num_tellers.release()
    num_customers.acquire()

def Customer(thread_id, action):
    print(f"Customer {thread_id} []: waiting to perform {action} transaction")
    num_tellers.acquire()
    num_customers.release() 


