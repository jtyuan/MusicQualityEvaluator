#!/usr/bin/python

import argparse
import csv
import os

import pandas as pd

from .evaluators import *

f = [pitch_class_set, pitch_diversity, rhythmic_diversity, measure_density]
w = [0.2, 0.2, 0.2, 0.2]


def get_score(s):
    # total = 0
    results = {}
    for i, t in enumerate(f):
        p = t(s)
        results[t.__name__] = p
        # total += w[i] * p
    # results['overall'] = total
    return results


def evaluate(o, output='output.csv'):
    with open(output, 'w') as csvfile:
        fieldnames = []
        for t in f:
            fieldnames.append(t.__name__)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0, len(o)):
            s = o.getScoreByNumber(i + 1)
            sc = get_score(s)
            # print(sc)
            writer.writerow(sc)
            csvfile.flush()

    df = pd.read_csv(output)
    print(df)


if __name__ == '__main__':

    parser = argparse.ArgumentParser('Evaluate a music piece')
    parser.add_argument('--file',
                        type=str,
                        help='Path to the file containing the music piece in ABC notation to evaluate.')
    parser.add_argument('--out',
                        type=str,
                        default='output.csv',
                        help='Scores will be written to this file in csv format.')

    argv = parser.parse_args()

    if not os.path.exists(argv.file):
        print('File does not exist: {}'.format(argv.file))

    print('Loading data from "{}"...'.format(argv.file))
    o = converter.parse(argv.file)
    evaluate(o)
