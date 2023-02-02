import time
import threading

# The threading can execute in background even if it the main thread is over, set "daemon" equal a True make his close when the "main threading" is finished 

def logged_time():
    count = 0
    while True:
        print(f"Time Logged is {count} seconds")
        time.sleep(1)
        count += 1


x = threading.Thread(target=logged_time, daemon=True)
x.start()

answer = input("Wish stay here? : \n")