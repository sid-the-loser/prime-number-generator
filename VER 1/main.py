try:
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
                primes.append(n)
                file.write(str(n)+"\n")

        n += 1

except KeyboardInterrupt:
    file.close()
    print(len(primes), ": prime numbers calculated!")
    print(count, ": new primes calculated!")
    print(n, ": biggest prime calculated!")