from pickle import dump

f = open("primes.txt", "r"); primes = f.read().split("\n"); del primes[-1];
for i in range(len(primes)):
    primes[i] = int(primes[i])
f = open("primes.dat", "wb"); dump(primes, f); f.close()
