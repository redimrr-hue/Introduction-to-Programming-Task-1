def even_or_odd(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

def main():
    num = int(input("Enter a number: "))
    result = even_or_odd(num)
    print(result)

main()