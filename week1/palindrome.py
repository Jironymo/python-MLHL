def is_palindrome(number):
    '''find out whether *number* is palindrome not using collections'''
    number_copy = number
    number_reversed = 0

    while number_copy > 0:
        current_digit = number_copy % 10
        number_reversed = number_reversed*10 + current_digit
        number_copy = number_copy // 10
    if number_reversed == number:
        print('is palindrome')
    else:
        print('not palindrome')
    
if __name__ == '__main__':
    while True:
        try:
            x = int(input('Provide integer: '))
        except ValueError:
            print('is not integer')
        else:
            break
        
    is_palindrome(x)