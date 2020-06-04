def main():
    #write your code below this line

    amount = 0

    while True:

        number = int(input("Enter a number: "))

        if number < 0:
            amount = amount + 1
        elif number == 0:
            print(f"Number of negative numbers: {amount}")

if __name__ == '__main__':
    main()
