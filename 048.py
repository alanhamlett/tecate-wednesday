"""Problem 48
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000."""

highest = 1000

total = 0
for n in range(1, highest):
    total += pow(n, n)
    print total
print total
