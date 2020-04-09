num = int(input("digite el numero:"))
def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num
print(perfect_number(num))

