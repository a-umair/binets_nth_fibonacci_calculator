import math
import sys


def find_nth_fibonacci_term(n):

    # precomputing square root of 5 to avoid recalculation when computing approximate value of nth term
    sqrt_5 = math.sqrt(5)

    PHI = (1 + sqrt_5) / 2  # golden ratio constant

    # precomputing PHI^n to avoid recalculation when computing approximate below
    phi_to_the_nth_power = PHI**n

    nth_term_approximate_value = (phi_to_the_nth_power -
                                  ((-1)**n)/phi_to_the_nth_power) / sqrt_5

    return int(nth_term_approximate_value)


if __name__ == '__main__':
    n = int(sys.argv[1])
    print("{0}th fibonacci term:\t {1}".format(n, find_nth_fibonacci_term(n)))
