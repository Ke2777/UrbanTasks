import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


filenames = [f'file {number}.txt' for number in range(1, 5)]


# Линейный вызов
def linear_read():
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    print("Линейное выполнение:", time.time() - start_time, "секунд")


# Многопроцессный вызов
def multiprocess_read():
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    print("Многопроцессное выполнение:", time.time() - start_time, "секунд")


if __name__ == '__main__':
    linear_read()
    multiprocess_read()
