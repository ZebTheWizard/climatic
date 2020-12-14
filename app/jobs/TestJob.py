# import time
# import threading 

# last = 0
# stop_threads = False


# def thread_func():
#     """ Count half seconds"""
#     while True:
#         global last
#         global stop_threads
        
#         last += 1
#         time.sleep(0.5)
        
#         if stop_threads: 
#             break

# thread = threading.Thread(target = thread_func)

# def job():
#     print("testing", last)

# def make(schedule):
#     global last
#     schedule.every().minutes.do(job)
#     thread.start()


# def destroy():
#     global stop_threads
#     stop_threads = True
#     thread.join()