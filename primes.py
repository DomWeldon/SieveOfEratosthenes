from typing import Generator, NewType, Optional

PrimeNumber = NewType("PrimeNumber", int)


def prime_generator(
    max_primes: Optional[int] = None
) -> Generator[PrimeNumber, None, None]:
    """Create a prime number generator using the Sieve of Eratosthenes."""
    # initialize a queue based on the first prime, keep track of max squares
    primes, n_max, n = [2], 2, -1

    # do we need to work out more primes?
    while max_primes is None or n <= max_primes:
        if n == len(primes) - 1:
            # yes, setup integers to square of last prime
            lp = primes[-1]
            n_max = lp ** 2
            integers = [True] * (n_max - lp)
            # sieve
            for f in primes:
                for i in range(f ** 2, n_max, f):  # change to reduce cycles?
                    integers[i - lp] = False
            primes.extend([i + lp for i, p in enumerate(integers) if p][1:])

        n += 1

        yield primes[n]

    return
