import multiprocessing
import random
import time
import datetime

def worker():
    # Wait for a random amount of time between 0 and 1 seconds
    time.sleep(random.random())
    
    # Print the current time
    now = datetime.datetime.now()
    print(f"Process {multiprocessing.current_process().name} exited at {now}")

if __name__ == "__main__":
    # Create three separate processes
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, name=f"Process {i}")
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()
