# yeah, i wrote it in one line 😆
from pickle import dump;primes = open("primes.txt", "r").read().split("\n"); del primes[-1];primes = [int(primes[i]) for i in range(len(primes))];f = open("primes.dat", "wb"); dump(primes, f); f.close()
