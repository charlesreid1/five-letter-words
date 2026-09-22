"""
prime_strings.py

Donald Knuth, Art of Computer Programming, Volume 4A, Section 7.2.1.1
Exercises #101 and #104

Definition P (p. 305): a string is prime if it is nonempty and
lexicographically less than all of its proper suffixes. (Lyndon word.)

Exercise 101: every string factors uniquely as l_1 l_2 ... l_t with
l_1 >= l_2 >= ... >= l_t, each l_j prime. Part (e) asks for the factors
of the first 40 digits of pi.

Exercise 104: about 1/n of all n-letter words are prime. How many of the
5757 SGB five-letter words are prime? Smallest nonprime? Largest prime?

Proofs are in prime_strings.md.
"""
import random
from get_words import get_words


PI40 = "3141592653589793238462643383279502884197"


def is_prime(s):
    """Definition P, verbatim: nonempty and less than every proper suffix."""
    return len(s) > 0 and all(s < s[i:] for i in range(1, len(s)))


def factor(s):
    """
    Factor s into nonincreasing primes in O(n) time.

    This is Duval's algorithm (J. Algorithms 4 (1983), 363-381), which
    Knuth gives as steps E4-E5 in the answer to exercise 106.

    Invariant: s[i:j] is a preprime (a prefix of a prime), namely the
    (j-i)-extension of the prime s[i:i+p] where p = j - k. Position k
    trails j by exactly p. When s[k] < s[j] the prefix s[i:j+1] becomes
    a new, longer prime (exercise 105(a)), so k resets to i. When
    s[k] > s[j] the preprime cannot be extended, and by exercise 105(b)
    s[i:i+p] is the first factor l_1; it repeats floor((j-i)/p) times.
    """
    n = len(s)
    factors = []
    i = 0
    while i < n:
        j, k = i + 1, i
        while j < n and s[k] <= s[j]:
            k = i if s[k] < s[j] else k + 1
            j += 1
        p = j - k
        while i <= k:
            factors.append(s[i:i + p])
            i += p
    return factors


def factor_greedy(s):
    """
    The existence proof of exercise 101(b), run literally: start from
    singletons and merge any adjacent pair l_j < l_{j+1}, which is prime
    by 101(a). Quadratic, used only as a cross-check for factor().
    """
    parts = list(s)
    merged = True
    while merged:
        merged = False
        for j in range(len(parts) - 1):
            if parts[j] < parts[j + 1]:
                parts[j:j + 2] = [parts[j] + parts[j + 1]]
                merged = True
                break
    return parts


def check_factorization(s, factors):
    """Every property exercise 101 promises."""
    assert "".join(factors) == s, s
    assert all(is_prime(f) for f in factors), (s, factors)
    assert all(a >= b for a, b in zip(factors, factors[1:])), (s, factors)
    assert factors == factor_greedy(s), (s, factors)


if __name__ == "__main__":

    print("-" * 40)
    print("Exercise 101(e): prime factors of the first 40 digits of pi")
    print(PI40)
    for f in factor(PI40):
        print("  " + f)

    print("-" * 40)
    print("Cross-check: Duval vs. definition vs. greedy merge on random strings")
    rng = random.Random(101)
    trials = 0
    for length in range(1, 13):
        for _ in range(500):
            s = "".join(rng.choice("012") for _ in range(length))
            check_factorization(s, factor(s))
            trials += 1
    for _ in range(2000):
        s = "".join(rng.choice("0123456789") for _ in range(rng.randint(1, 40)))
        check_factorization(s, factor(s))
        trials += 1
    print("{0:d} random strings factored consistently.".format(trials))

    print("-" * 40)
    print("Exercise 104: prime five-letter words in the SGB")
    words = sorted(get_words())
    primes = [w for w in words if is_prime(w)]
    nonprimes = [w for w in words if not is_prime(w)]
    print("{0:d} words total.".format(len(words)))
    print("{0:d} prime, {1:d} nonprime.".format(len(primes), len(nonprimes)))
    print("Eq. (60) estimate, 1/5 of all words: {0:d}".format(len(words) // 5))
    print("Smallest nonprime: {0:s}".format(nonprimes[0]))
    print("Largest prime:     {0:s}".format(primes[-1]))
    print("First few nonprimes: " + ", ".join(nonprimes[:3]))
    print("Last few primes:     " + ", ".join(primes[-3:]))
    for w in ("prime", "lowly", "first", "knuth"):
        print("  {0:s} is {1:s}prime, factors {2!s}".format(
            w, "" if is_prime(w) else "not ", factor(w)))
