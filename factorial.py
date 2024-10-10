def factorial(Tnum): 
        num = float(Tnum)
        val = num
        while val > 1:
            val-=1
            num = num*val
        print(num)
while True:
    number = input('Enter your number ')
    factorial(number)


