TEXT = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
        7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
        13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
        50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 10**12: "one trillion"}
W = [[100, "hundred"], [1000, "thousand"], [10**6, "million"], [10**9, "billion"], [10**12, "trillion"]]


def num_to_text(n):
    if n in TEXT:
        return TEXT[n]
    if n < 100:
        return "{} {}".format(num_to_text(n - n % 10), num_to_text(n % 10))
    l = len(W)
    for i in range(l):
        if W[i][0] <= n < W[i+1][0]:
            if n % W[i][0] == 0:
                return "{} {}".format(num_to_text(n//W[i][0]), num_to_text(W[i][1]))
            else:
                return "{} {} {}".format(num_to_text(n//W[i][0]), W[i][1], num_to_text(n % W[i][0]))

T = int(input())
for i in range(T):
    N = int(input())
    print(' '.join([c[0].upper() + c[1:] for c in num_to_text(N).split()]))
