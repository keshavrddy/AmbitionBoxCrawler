import threading
from queue import Queue
import time
from ambition import Companyreviews as company
from connectionmanager import Connectionmanager

print_lock = threading.Lock()
input_url = open('source.txt', 'r', encoding='utf-8').readlines()


def job(worker):
    try:
        data = company(input_url[worker])
        print(input_url[worker], threading.current_thread().name, worker)
        # print(type(data))
    except Exception:
        file = open('404urls.txt', 'a', encoding='utf-8')
        file.write(input_url[worker] + '\n')
        file.close()
        data = ''
    return data


def writetofile(data):
    if data:
        file = open('ambitionboxData.txt', 'a', encoding='utf-8')
        file.write(data.__str__() + '\n')
        file.close()



def threader():

    while True:

        worker = q.get()

        try:
            ratings = job(worker)
            writetofile(ratings)
        except Exception as e:
            print e
            # Get new identity
            Connectionmanager()

        q.task_done()

q = Queue()

start = time.time()

for i in range(20):

    t = threading.Thread(target=threader)

    t.daemon = True

    t.start()

for worker in range(len(input_url) - 1):
    q.put(worker)

q.join()

print('Entire job took:',time.time() - start)

