__author__ = 'Marc Bickel'

import pandas as pd
import argparse
import os

__created__ = '05.08.2015'


def parse_args():
    description = 'Parse CSV files and stack them by their matching columns. '
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('input_files',
                        nargs='+',
                        help='List of csv-files, separated by comma.')

    parser.add_argument('--delimiter',
                        default=';',
                        help=('CSV-delimiter '
                              '(default: \'%(default)s\')'))

    parser.add_argument('--encoding',
                        default='utf-8',
                        help=('Encoding of CSV-files '
                              '(default: \'%(default)s\')'))

    parser.add_argument('--output',
                        default='out.csv',
                        help=('Output-file '
                              '(default: \'%(default)s\')'))

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    dat = []

    # parse all input files
    for f in args.input_files:
        dat.append(pd.read_csv(os.path.normpath(f.strip()), sep=args.delimiter, encoding=args.encoding))

    # combine them by matching columns
    pd.concat(dat).to_csv(args.output, sep=args.delimiter, encoding=args.encoding)

    print('Done.')


if __name__ == '__main__':
    main()
