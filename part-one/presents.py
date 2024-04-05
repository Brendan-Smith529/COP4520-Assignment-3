import multiprocessing as mp, time
import queue

from random import randint, shuffle

from ConcurrentLinkedList import ConcurrentLinkedList

N_PRESENTS = 500_000
N_THREADS = 4

# Shared list
linked_list = ConcurrentLinkedList()

# Present bag
present_bag_list = list(range(N_PRESENTS))
shuffle(present_bag_list)

present_bag = queue.Queue()
map(present_bag.put, present_bag_list)

# Actions
def select_random(counter, lock):
    while counter.value < N_PRESENTS:
        num = randint(0, 2)

        match num:
            case 0:
                take_present(lock)
            
            case 1:
                write_card(counter)

            case 2:
                check_for_tag(lock)

def take_present(lock):
    with lock:
        if present_bag.qsize() > 0:
            linked_list.append(present_bag.peek())

            present_bag.popleft()

def write_card(counter):
    linked_list.remove()

    with counter.get_lock():
        counter.value += 1

def check_for_tag(lock):
    index = randint(0, N_PRESENTS - 1)

    with lock:
        linked_list.search(index)


if __name__ == "__main__":
    threads = []
    
    start_time = time.time()

    counter = mp.Value('i', 0, lock=True);
    lock = mp.Lock()

    # Spawns threads
    for _ in range(N_THREADS):
        thread = mp.Process(target=select_random, args=(counter, lock))
        thread.start()
        threads.append(thread)

    # Joins threads
    for thread in threads:
        thread.join()

    elapsed_time = time.time() - start_time
    print(f'complete in {elapsed_time:.2f} seconds')

