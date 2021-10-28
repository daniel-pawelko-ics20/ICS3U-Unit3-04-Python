#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Oct 2021
# This program outputs if input is positive negative or just zero


def main():
    # This function inputs integer and outputs if intereger is pos, neg or zero
    # input
    integer = int(input("Enter an integer: "))

    # process/output
    if integer > 0:
        print(f"{integer} is a positive number.")
    elif integer < 0:
        print(f"{integer} is a negative number.")
    else:
        print("0 is just zero!")

    # output finished
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
