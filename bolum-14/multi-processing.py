import time
import multiprocessing

def calculate_square(numbers,liste):
    for index,value in enumerate(numbers):
        time.sleep(0.3)
        # print("kare:", i * i)
        liste[index] = value * value

def calculate_cube(numbers,liste):
    for index,value in enumerate(numbers):
        time.sleep(0.3)
        # print("küpü:", i * i * i)
        liste[index] = value * value * value

if __name__ == "__main__":
    arr = [2,4,6,8,12,56,126,256,24555]
    
    t = time.time()

    liste_square = multiprocessing.Array('i', 9)
    liste_cube = multiprocessing.Array('i', 9)

    p1 = multiprocessing.Process(target=calculate_square, args=(arr,liste_square,))
    p2 = multiprocessing.Process(target=calculate_cube, args=(arr,liste_cube,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(time.time()- t)

    print(liste_square[:])
    print(liste_cube[:])

