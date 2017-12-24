import sys
import threading
import multiprocessing
import time
import math
import os
import numpy


__author__ = 'ericmiller'


class Prime:
    def __init__(self):
        pass

    @staticmethod
    def get_primes(max_prime):
        if max_prime < 3:
            return -1
        known_primes = [2, 3]
        index = 5
        for i in range(index, max_prime, 2):
            is_prime = True

            relevant_primes = filter(lambda p: p ** 2 <= i, known_primes)
            for prime in relevant_primes:
                if i % prime == 0:
                    is_prime = False
                    break

            if is_prime:
                yield i

    @staticmethod
    def sieve_of_atkin(max_prime):
        limit = max_prime
        sieve = [False] * limit
        for x in range(1, limit):
            x2 = x ** 2
            if x2 >= limit:
                break

            for y in range(1, limit):
                y2 = y ** 2
                if y2 >= limit:
                    break

                n = 4 * x2 + y2
                if n <= limit and (n % 12 == 1 or n % 12 == 5):
                    sieve[n] ^= True

                _3x2 = 3 * x2
                n = _3x2 + y2
                if n <= limit and n % 12 == 7:
                    sieve[n] ^= True

                n = _3x2 - y2
                if x > y and n <= limit and n % 12 == 11:
                    sieve[n] ^= True

        # We've made it through the main sieve.
        # Mark all multiples of squares as non-prime.
        limit_sqrt = int(math.sqrt(limit)) + 1
        for (r, r2) in map(lambda r: (r, int(r ** 2)), range(5, limit_sqrt)):
            if sieve[r]:
                for i in range(r2, limit, r2):
                    sieve[i] = False

        for a in range(1, limit):
            if sieve[a]:
                yield a


class SieveOfAtkin():
    def __init__(self, limit, threads=None):
        self.started = False
        self.all_jobs_queued = False
        self.limit = limit
        self.limit_sqrt = int(math.sqrt(self.limit)) + 1
        print("Filling Sieve...")
        self.sieve = [False] * self.limit
        self.job_queue = multiprocessing.Queue(1000)

        print("Initializing Job Queue with %d jobs..." % (limit-1))

        def fill_jobs():
            for x in range(1, self.limit):
                if self.job_queue.full():
                    time.sleep(2)
                self.job_queue.put(x)
            self.all_jobs_queued = True

        if threads is None or threads < 1:
            self.threads = min(os.cpu_count(), int(self.limit / 2) + 1)
        else:
            self.threads = threads

        print("Starting %d threads..." % self.threads)
        self.workers = []
        for i in range(self.threads):
            worker = multiprocessing.Process(target=self.__worker, args=[self.job_queue])
            self.workers.append(worker)

        print("Setting up Mutex...")
        self.sieve_mutex = threading.Lock()
        self.queue_mutex = threading.Lock()

        print("Waiting for initialization threads to finish up...")
        fill_jobs()

    def __worker(self, queue):
        while True:
            self.queue_mutex.acquire()
            if queue.empty() and self.all_jobs_queued:
                self.queue_mutex.release()
                break
            x = queue.get()
            self.queue_mutex.release()

            x2 = x ** 2
            if x2 >= self.limit:
                continue

            for y in range(1, self.limit):
                y2 = y ** 2
                if y2 >= self.limit:
                    break

                n = 4 * x2 + y2
                if n <= self.limit and (n % 12 == 1 or n % 12 == 5):
                    self.toggle_sieve(n)

                _3x2 = 3 * x2
                n = _3x2 + y2
                if n <= self.limit and n % 12 == 7:
                    self.toggle_sieve(n)

                n = _3x2 - y2
                if x > y and n <= self.limit and n % 12 == 11:
                    self.toggle_sieve(n)
        print("Worker done.")
        print(self.sieve)

    def start(self):
        if self.started:
            return
        self.started = True
        for w in self.workers:
            w.start()

    def get_primes(self):
        self.start()
        print("Waiting for workers.")
        for w in self.workers:
            w.join()

        print("Sieve of Atkin is finishing up some work.")

        for (r, r2) in map(lambda r: (r, int(r ** 2)), range(5, self.limit_sqrt)):
            if self.sieve[r]:
                for i in range(r2, self.limit, r2):
                    self.set_sieve(i, False)

        print(self.sieve)
        for a in range(0, self.limit):
            if self.sieve[a]:
                yield a

    def toggle_sieve(self, key):
        self.sieve_mutex.acquire()
        self.sieve[key] ^= True
        self.sieve_mutex.release()

    def set_sieve(self, key, value):
        self.sieve_mutex.acquire()
        self.sieve[key] = value
        self.sieve_mutex.release()
