# def dec_selamlama(count):
#     def selamlama(fn):
#         def inner(ad):
#             for _ in range(count):
#                 fn(ad)
#         return inner
#     return selamlama

# @dec_selamlama(count=2)
# def gunaydin(ad):
#     print(f"günaydın benim adım {ad}")

# @dec_selamlama(count=3)
# def iyigunler(ad):
#     print(f"iyi günler benim adım {ad}")
    
# gunaydin("Ali")
# iyigunler("Sadık")

import time

def dec_speed_test(count):
    def speed_test(fn):
        def inner(*args, **kwargs):
            start_time = time.perf_counter()
            print(f"{fn.__name__} metodu çalışıyor.")
            for _ in range(count):
                result = fn(*args, **kwargs)
                end_time = time.perf_counter()
                run_time = end_time - start_time
                print(f"geçen süre: {run_time}")
            return result
        return inner
    return speed_test

@dec_speed_test(count=2)
def sum_gen():    
    return sum((x for x in range(10000000)))

@dec_speed_test(count=3)
def sum_list():
    return sum([x for x in range(10000000)])


print(sum_gen())
print(sum_list())
