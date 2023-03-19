import math


start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))


for i in range(start, end+1):

    if math.isqrt(i)**2 == i:

        digit_sum = sum(int(digit) for digit in str(i))

        if digit_sum < 10:
            print(i)
