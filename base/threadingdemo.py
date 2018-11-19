from threading import Thread
threads = []
def demo():
    print("111")
for i in range(1, 5):
    t = Thread(demo())
    t.start()
    threads.append(t)
for t in threads:
    t.join()
