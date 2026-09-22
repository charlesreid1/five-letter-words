"""
prime_strings.py

Donald Knuth, Art of Computer Programming, Volume 4A, Section 7.2.1.1
Exercises #101, #102 and #104

Definition P (p. 305): a string is prime if it is nonempty and
lexicographically less than all of its proper suffixes. (Lyndon word.)

Exercise 101: every string factors uniquely as l_1 l_2 ... l_t with
l_1 >= l_2 >= ... >= l_t, each l_j prime. Part (e) asks for the factors
of the first 40 digits of pi.

Exercise 102: deduce L_m(n), the number of m-ary primes of length n, from
the unique factorization theorem. Answer: eq. (60), L_m(n) =
(1/n) sum_{d | n} mu(d) m^(n/d).

Exercise 104: about 1/n of all n-letter words are prime. How many of the
5757 SGB five-letter words are prime? Smallest nonprime? Largest prime?

Proofs are in prime_strings.md.
"""
import random
from itertools import product
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


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    """Moebius function mu(n) by trial division."""
    result = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            result = -result
        p += 1
    if n > 1:
        result = -result
    return result


def num_primes(m, n):
    """
    L_m(n), the number of m-ary prime strings of length n, by eq. (60):
    L_m(n) = (1/n) sum over d | n of mu(d) m^(n/d).
    Derived from the factorization theorem in prime_strings.md, ex. 102.
    """
    return sum(mobius(d) * m ** (n // d) for d in divisors(n)) // n


def num_primes_brute(m, n):
    """Count m-ary primes of length n directly from Definition P."""
    return sum(1 for s in product(range(m), repeat=n) if is_prime(s))


def euler_product_coefficients(m, N):
    """
    Coefficients of z^0 .. z^N in prod_{n>=1} (1 - z^n)^(-L_m(n)).

    Each factor 1/(1 - z^n) chooses how many copies of one particular
    prime of length n go into the multiset, so the coefficient of z^N
    counts multisets of primes with total length N. By exercise 101
    those multisets are in bijection with the m^N strings of length N.
    """
    c = [1] + [0] * N
    for n in range(1, N + 1):
        for _ in range(num_primes(m, n)):
            for i in range(n, N + 1):
                c[i] += c[i - n]
    return c


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
    print("Exercise 102: L_m(n), the number of m-ary primes of length n")
    print("n:      " + " ".join("{0:5d}".format(n) for n in range(1, 11)))
    for m in (2, 3, 4):
        print("L_{0:d}(n): ".format(m)
              + " ".join("{0:5d}".format(num_primes(m, n)) for n in range(1, 11)))
    print("Checks:")
    checks = 0
    for m in (2, 3, 4):
        for n in range(1, 9):
            if m ** n <= 70000:
                assert num_primes(m, n) == num_primes_brute(m, n), (m, n)
                checks += 1
    print("  eq. (60) equals brute-force count in {0:d} (m, n) cases".format(checks))
    for m in (2, 3, 4, 10):
        for n in range(1, 13):
            assert sum(d * num_primes(m, d) for d in divisors(n)) == m ** n
    print("  eq. (59), sum of d L_m(d) over d | n = m^n, holds for m in 2,3,4,10 and n <= 12")
    for m in (2, 3):
        N = 12
        assert euler_product_coefficients(m, N) == [m ** n for n in range(N + 1)]
    print("  Euler product prod (1 - z^n)^(-L_m(n)) = 1/(1 - mz) through z^12 for m = 2, 3")
    print("L_26(5) = {0:d} of the 26^5 = {1:d} five-letter strings are prime, "
          "fraction {2:.4f}".format(num_primes(26, 5), 26 ** 5,
                                    num_primes(26, 5) / 26 ** 5))

    print("-" * 40)
    print("Exercise 104: prime five-letter words in the SGB")
    words = sorted(get_words())
    primes = [w for w in words if is_prime(w)]
    nonprimes = [w for w in words if not is_prime(w)]
    print("{0:d} words total.".format(len(words)))
    print("{0:d} prime, {1:d} nonprime.".format(len(primes), len(nonprimes)))
    print("Eq. (60) estimate, 1/5 of all words: {0:d}".format(len(words) // 5))
    print("Fraction of SGB words that are prime: {0:.4f}".format(len(primes) / len(words)))
    print("Smallest nonprime: {0:s}".format(nonprimes[0]))
    print("Largest prime:     {0:s}".format(primes[-1]))
    print("First few nonprimes: " + ", ".join(nonprimes[:3]))
    print("Last few primes:     " + ", ".join(primes[-3:]))
    for w in ("prime", "lowly", "first", "knuth"):
        print("  {0:s} is {1:s}prime, factors {2!s}".format(
            w, "" if is_prime(w) else "not ", factor(w)))
