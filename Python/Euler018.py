#!/usr/bin/env python3
import Euler011


def main():
    print(get_biggest_triangle_sum('input/Euler018.txt'))


def get_biggest_triangle_sum(of_file):
    triangle = Euler011.load_file(of_file)

    for row in reversed(range(0, len(triangle) - 1)):
        for col in range(0, len(triangle[row])):
            lchild = triangle[row+1][col]
            rchild = triangle[row+1][col+1]

            if lchild > rchild:
                triangle[row][col] += lchild
            else:
                triangle[row][col] += rchild

    return triangle[0][0]


if __name__ == '__main__':
    main()
