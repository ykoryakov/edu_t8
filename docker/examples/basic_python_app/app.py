import argparse
import numpy as np


def main_0():
    a = np.zeros((3, 3), dtype=np.uint8)
    b = a + 10
    print(b)


def main_1():
    parser = argparse.ArgumentParser(description='App service.')
    parser.add_argument('--n', type=int, help='Array shape n.', default=3)
    args = parser.parse_args()

    a = np.zeros((args.n, args.n), dtype=np.uint8)
    b = a + 10
    print(b)


if __name__ == '__main__':

    # main_0()
    main_1()
