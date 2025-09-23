def i_hate_math(a, b):
    if b == 1:
        return a
    return a * i_hate_math(a, b-1)


i_hate_math(2, 3)


def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n-1)


print(sum_to_n(5))


def reverse_string(s):
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]


print(reverse_string("hello"))
