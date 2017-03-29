__author__ = 'ericmiller'


def main():
    base_num = 1
    total_found = 0

    while base_num < 987654321:
        i = 1
        pandigital = str(base_num)
        while len(pandigital) < 9:
            i += 1
            pandigital += str(i * base_num)

        if i == 1:
            break

        # Check that all the digits are there
        has_all_digits = len(pandigital) == 9
        for digit in range(1, 10):  # end is exclusive
            has_all_digits = has_all_digits and (str(digit) in pandigital)

        if has_all_digits:
            total_found += 1
            print "base: " + str(base_num) + ", n: " + str(i) + ", Pandigital: " + str(pandigital)

        base_num += 1

    print "found: " + str(total_found)

main()
