#Write a function called exponent(base, exp)
# that returns an int value of base raises to the power of exp.

# function
def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    return result

# user input
base = int(input('enter a number:'))
exp = int(input('enter a power:'))






