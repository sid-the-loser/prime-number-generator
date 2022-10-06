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
n_ = 0
running =True

for i in range(count_):
    primes[i] = int(primes[i])

def output():
    global running, primes, count, n_, file
    try:
        while running:
            print(f"----------------------------------------\n{count} : new primes calculated!\n{count_} : prime numbers calculated!\n{n_} : biggest prime calculated!\n----------------------------------------")
            sleep(1)
            try:
                run('cls')
            except:
                try:
                    run('clear')
                except:
                    print("\n"*1000)

        print("BYE!")
    except KeyboardInterrupt:
        file.close()
        running = False
    
start_new_thread(output, ())

try:
    while True:
        flag = True
        for j in primes:
            if j > 1 and n//2 >= j:
                if (n%j == 0 and n != j and j < n) or (n%2 == 0):
                    flag = False
                    break
            else:
                break

        if flag:
            if not n in primes:
                count += 1
                count_ += 1
                n_ = n
                primes.append(n)
                file.write(str(n)+"\n")
                file.flush()

        n += 1

except KeyboardInterrupt:
    file.close()
    running = False