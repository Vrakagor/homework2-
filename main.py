def main():

    number = int(input("Введіть 4-х значне число: "))

    digit1, remainder = divmod(number, 1000)
    digit2, remainder = divmod(remainder, 100)
    digit3, digit4 = divmod(remainder, 10)

    print(digit1)
    print(digit2)
    print(digit3)
    print(digit4)

if __name__ == "__main__":
    main()
