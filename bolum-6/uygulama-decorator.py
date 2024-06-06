import time

def speed_test(fn):
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        print(f"{fn.__name__} metodu çalışıyor.")
        result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"geçen süre: {run_time}")
        return result
    return inner

@speed_test
def sum_gen():    
    return sum((x for x in range(100000000)))

@speed_test
def sum_list():
    return sum([x for x in range(100000000)])


print(sum_gen())
print(sum_list())
