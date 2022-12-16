def square_sum_minus_sum_squares(n):
    sum = 0
    sum_squares = 0
    for digit in range(1,n+1):
        sum_squares += digit**2
        sum += digit
    
    return sum**2 - sum_squares

print(square_sum_minus_sum_squares(100))
