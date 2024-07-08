def is_power_of_two(n):
    return n > 0 and not (n & (n - 1))

def is_thabit_no(n):
    n += 1
    if n % 3 == 0:
        n //= 3
    else:
        return False
    return is_power_of_two(n)

n = int(input("Enter a number : "))
if is_thabit_no(n):
    print(f"{n} is a Thabit number.")
else:
    print(f"{n} is not a Thabit number.")
