import multiprocessing as mp, time
from random import randint

N_THREADS = 8

LOW = -100
HIGH = 70
MINUTES = 60
INTERVAL = 10

def get_temps(temp_list, lock):
    low = HIGH + 1
    high = LOW - 1

    for _ in range(MINUTES):
        temp = randint(-100, 70)

        with lock:
            temp_list.append(temp)

def get_biggest_diff(temp_list):
    max_diff = 0

    for i in range (MINUTES - INTERVAL):
        temps = temp_list[i: i + INTERVAL]
        min_temp = min(temps)
        max_temp = max(temps)
        new_diff = max_temp - min_temp

        if new_diff > max_diff:
            max_diff = new_diff

    return max_diff


if __name__ == "__main__":
    threads = []

    with mp.Manager() as manager:
        temp_list = manager.list()
        lock = manager.Lock()
        
        start_time = time.time()

        # Spawns threads
        for _ in range(N_THREADS):
            thread = mp.Process(target=get_temps, args=(temp_list, lock))
            thread.start()
            threads.append(thread)

        # Joins threads
        for thread in threads:
            thread.join()

        low = min(temp_list)
        high = max(temp_list)
        largest_diff = get_biggest_diff(temp_list)

        print(f'Lowest Temp:\t{low}')
        print(f'Highest Temp:\t{high}')
        print(f'Largest Gap:\t{largest_diff}')

    print('-' * 75)

    elapsed_time = time.time() - start_time
    print(f'complete in {elapsed_time:.2f} seconds')
