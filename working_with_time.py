import time

print(time.time())


def send_msg():
    for i in range(10000):
        pass


start = time.time()
send_msg()
end = time.time()

print(end - start)
