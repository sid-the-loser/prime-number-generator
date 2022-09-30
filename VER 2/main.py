from _thread import start_new_thread
from time import sleep
from os import system as run

filename = "primes.txt"

try:
    open(filename, "r")
except:
    open(filename, "x").close()

file = open(filename, "r")
primes = file.read().split("\n")
print("Old file loaded or new file generated!")
del primes[-1]
if primes != None and len(primes) > 0:
    n = int(primes[-1])+1
else:
    n = 2
    primes = []
file = open(filename, "a")
count = 0
count_ = len(primes)
running =True

def output():
    global running, primes, count, n, file
    try:
        while running:
            print("----------------------------------------")
            print(count, ": new primes calculated!")
            print(count_, "prime numbers calculated!")
            print(n, ": biggest prime calculated!")
            print("----------------------------------------")
            sleep(0.2)
            try:
                run('cls')
            except:
                try:
                    run('clear')
                except:
                    pass

        print("BYE!")
    except KeyboardInterrupt:
        file.close()
        running = False
    
start_new_thread(output, ())

try:
    while True:
        flag = True
        for i in primes:
            j = int(i)
            if j > 1:
                if (n%j == 0 and n != j and j < n) or (n%2 == 0):
                    flag = False
                    break

        if flag:
            if not n in primes:
                count += 1
                count_ += 1
                primes.append(n)
                file.write(str(n)+"\n")

        n += 1

except KeyboardInterrupt:
    file.close()
    running = False