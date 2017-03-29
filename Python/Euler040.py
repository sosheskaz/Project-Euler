__author__ = 'ericmiller'


def main():
    string = "."
    for i in range(1, 1000000):
        string += str(i)

    result = 1
    result *= int(string[1])
    result *= int(string[10])
    result *= int(string[100])
    result *= int(string[1000])
    result *= int(string[10000])
    result *= int(string[100000])
    result *= int(string[1000000])
    print result


main()
