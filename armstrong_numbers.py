def is_armstrong(number):
    num_str = str(number)
    power = len(num_str)
    num_sum = sum([int(digit)**power for digit in num_str])
    return num_sum == number 
