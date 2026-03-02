############# MULTITHREADING ##############

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

def mian():
    time1 = time.perf_counter()

    #using simle function call
    # func(4)
    # func(2)
    # func(1)


    # same code using threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    t1.start() #this will just tell the start time and if not using join, it will make it look like program has ended
    t2.start()
    t3.start()

    t1.join() # this ends the program time. we can see the slowest thread is 4 seconds, output is 4 too
    t2.join()
    t3.join()


    time2 = time.perf_counter()
    print(time2 - time1)

def PoolingDemo():

    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 4)
        # print(future1.result())
        # future2 = executor.submit(func, 2)
        # print(future2.result())
        # future3 = executor.submit(func, 3)
        # print(future3.result())
        
        time3 = time.perf_counter()
        l = [3,5,2,3,1]
        results = executor.map(func, l)
        for result in results:
            print(result)
        time4 = time.perf_counter()
        print(time4 - time3)
PoolingDemo()

