lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

possibleids = [l1+l2+num1+num2 for l1 in lowercase for l2 in lowercase for num1 in digits for num2 in digits]

print(possibleids)