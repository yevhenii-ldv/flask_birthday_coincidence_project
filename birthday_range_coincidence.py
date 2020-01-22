import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--drange', default=7, type=int)
    parser.add_argument('--pcnt', default=8, type=int)
    parser.add_argument('--ydays', default=365, type=int)

    return parser


def funct_birthday(drange, pcnt, ydays):
    multipli = 1
    for i in range(1, pcnt):
        multipli *= 1-((i+drange)/ydays)

    return round((1 - multipli)*100, 6)


if __name__ == "__main__":
    parser = create_parser()
    name_space = parser.parse_args(sys.argv[1:])
    answer = funct_birthday(name_space.drange,
                            name_space.pcnt,
                            name_space.ydays)
    print(f'The probability that among {name_space.pcnt} people in a room, the birthdays of at least one couple differ'
          f' by less than {name_space.drange} days with {name_space.ydays} days a year is {answer} percent.')
