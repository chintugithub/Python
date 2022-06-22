def two_numbers_sum(targetsum, num):
    for number1 in num:
        number2 = targetsum - number1
        if number2 in num:
            print(number1,number2)
        
two_numbers_sum(5,[1,2,3,7,4])