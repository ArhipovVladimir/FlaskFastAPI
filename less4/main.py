import threading
import time
import multiprocessing
def worker(num):
    print(f"Начало работы потока {num}")
    time.sleep(3)
    print(f"Конец работы потока {num}")


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i, ))
    threads.append(t)
    t.start()


for t in threads:
    t.join()
    print("Все потоки завершили работу")



counter = 0
def increment():

    global counter

    for _ in range(1_000_000):
        counter += 1
    print(f"Значение счетчика: {counter:_}")


threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Значение счетчика в финале: {counter:_}")




def worker(num):
    print(f"Запущен процесс {num}")
    time.sleep(3)
    print(f"Завершён процесс {num}")


if __name__ == '__main__':
    processes = []

    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
        print("Все процессы завершили работу")


#
# counter = multiprocessing.Value('i', 0)
# def increment(cnt):
#
#     for _ in range(10_000):
#         with cnt.get_lock():
#         cnt.value += 1
#     print(f"Значение счетчика: {cnt.value:_}")
#
# if __name__ == '__main__':
#
#     processes = []
#     for i in range(5):
#         p = multiprocessing.Process(target=increment, args=(counter, ))
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()
#     print(f"Значение счетчика в финале: {counter.value:_}")