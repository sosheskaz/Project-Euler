def main():
    s = 0
    for j in range(1, 1001):
        s += j ** j
    print(str(s)[-10:])


if __name__ == '__main__':
    main()
