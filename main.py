import threading

# функція для відрахунку
def countdown_back(number):
    from time import sleep

    for i in range(number, 0, -1):
        print(i)
        sleep(1)

# функція для запуску окремого потоку
def countdown(number):
    t = threading.Thread(target=countdown_back, args=(number,))
    t.start()


countdown(4)
countdown(4)
countdown(4)
