def factorialTrailingZeros(n):

    number = 1
    k = 1
    for i in range(1,n+1):
        number *= i

    number = str(number)


   ## print(number)
    for i in range(len(number)-1):
        if number[i] == '0' and number[i+1] == '0':
            k = k+1

    return k



print(factorialTrailingZeros(10))
print(factorialTrailingZeros(29))
