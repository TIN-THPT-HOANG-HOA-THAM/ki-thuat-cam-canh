def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

chuoi = "str12ch3in7uoi456ing"
res = []

number = ""
for char in chuoi:
    if char.isdigit():
        number += char
    elif number != "":
        if is_prime(int(number)):
            res.append(int(number))
        number = ""
print(res)
