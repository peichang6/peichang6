def calculate(min, max):
    i = min
    ans = 0
    while i <= max:
        ans += i
        i += 1
    print(ans)


calculate(1, 3)
calculate(4, 8)
