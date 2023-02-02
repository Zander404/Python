import threading
import time

def eat():
    time.sleep(5)
    print("You eat")

def shower():
    time.sleep(4)
    print("You take a shower")

def stop():
    time.sleep(10)
    print("You stay stop for no reason")
    

x = threading.Thread(target=eat) # Create a new Thread dedicated for execute that fuction
x.start()

y = threading.Thread(target=shower)
y.start()
z = threading.Thread(target=stop)
z.start()


x.join() # Wait the thread finished before executate next line
y.join()
z.join()



print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter()) 
# help(threading)