help_text = """
h - help
s - save/backup
as - set autosave time (seconds)
x - exit program
cls - clear screen in windows
clear - clear screen in linux, etc.
p - pause prime number calculation
st - status on prime number calculation
e - backup and export the current primenumbers as a text file"""

import threading
from os import system as run
from pickle import dump, load
from time import time

filename = "primes.dat"
name = "HPC"
auto_save = 60
saving = False
pause = False

try:
    f = open(filename, "rb")
except FileNotFoundError:
    f = open(filename, "wb")
    dump([2, 3], f)
    f.close()
    f = open(filename, "rb")

try:
    primes = load(f)
except EOFError:
    primes = [2]

length = len(primes)
biggest = primes[-1]
n = biggest
new_length = 0

running = True

def say(text:str, end="\n"):
    print(f"{name}<< {text}", end=end)

def backup():
    global filename, primes, saving
    if not saving:
        saving = True
        say(f"Backing up to {filename}...")
        f = open(filename, "wb")
        say("Cleared past backup data...")
        dump(primes.copy(), f)
        say("Dumped data to temporary storage...")
        f.close()
        say(f"Saved to {filename} file!")
        saving = False
    else:
        say("Prime numbers are being backed up! Please wait!")

def secondary():
    global running, name, auto_save, help_text, biggest, length, new_length, n, saving, pause
    say("Type 'h' for help!")
    while running:
        a = input(f"{name}>> ").lower()
        if a == "h":
            say(help_text)
        elif a == "s":
            backup()
        elif a == "as":
            say(f"Time between each auto-save (seconds, currently: {auto_save}): ", end="")
            try:
                auto_save = float(input())
            except TypeError:
                pass
        elif a == "x":
            backup()
            running = False
        elif a == "cls":
            run("cls")
        elif a == "clear":
            run("clear")
        elif a == "p":
            pause = not pause
            say(f"Prime number processing, paused: {pause}")
        elif a == "st":
            for i in f"Biggest prime number: {biggest}\nTotal prime numbers calculated:\n\tNew: {new_length}\n\tHistory:{length}\nCurrently checking: {n}\nPaused: {pause}".split("\n"):
                say(i)
        elif a == "e":
            backup()
            if not saving:
                say(f"Opening {filename}...")
                f = open(filename, "rb")
                say(f"Loading data from {filename}...")
                data = load(f)
                f.close()
                say(f"Opening {filename}.txt...")
                f = open(filename+".txt", "w")
                say(f"Writing data to {filename}.txt...")
                for i in data:
                    f.write(str(i)+"\n")
                say(f"Flushing data to {filename}.txt")
                f.close()
                say("Export successful!")
            else:
                say("Export failed!")
        else:
            say("Please type 'h' command for help!")

def tertiary():
    global running, auto_save
    start_time = time()
    while running:
        if time() - start_time > auto_save:
            start_time = time()
            backup()

def primary():
    global running, pause, n, length, primes, biggest, new_length
    while running:
        if not pause:
            n += 2
            flag = True
            for i in primes:
                if n % i == 0:
                    flag = False
                    break
                elif n//2 < i:
                    break
                
            if flag:
                primes.append(n)
                length += 1; new_length += 1; biggest = n

t1 = threading.Thread(target=primary)
t2 = threading.Thread(target=secondary)
t3 = threading.Thread(target=tertiary)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()