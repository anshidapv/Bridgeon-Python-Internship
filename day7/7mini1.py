import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"time taken: {end-start:.4f} seconds")
    return wrapper
@timer
def count_to_million():
    for i in range(1000000):
        pass
count_to_million()