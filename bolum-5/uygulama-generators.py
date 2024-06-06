# (1 - ∞) aralığındaki her sayının karesini getiren fonksiyon.
# Fibonacci serisini hem normal fonksiyon hem de generator fonksiyon ile oluşturun.
# Performans testlerini yapın.

# def sayi_uret():
#     sayi = 0
#     while True:
#         yield sayi ** 2
#         sayi += 1

# generator = sayi_uret()

# print(next(generator))
# print(next(generator))
# print(next(generator))

# for i in generator:
#     print(i)

def fib_list(max):
    sayilar = []

    a, b = 0, 1

    while len(sayilar) <= max:
        sayilar.append(b)
        a, b = b, a + b

    return sayilar

# print(fib_list(9000))

def fib_gen(max):
    a, b = 0, 1
    count = 0
    while count <= max:
        a, b = b, a + b
        yield b
        count += 1

# for i in fib_gen(9000):
#     print(i)

import sys  

liste = [i for i in range(10000)]
print(sys.getsizeof(liste))

gen = (i for i in range(10000))
print(sys.getsizeof(gen))

import time

list_start_time = time.time()
sum([i for i in range(9000000)])
list_stop = time.time() - list_start_time

gen_start_time = time.time()
sum((i for i in range(9000000)))
gen_stop = time.time() - gen_start_time

print(list_stop)
print(gen_stop)