#!/usr/bin/python
# -*- coding: UTF-8 -*-
# top 5 words in a file


from __future__ import print_function
from collections import Counter


def generate_dict(filename):
    words_dict = Counter()
    with open(filename) as f:
        for line in f:
            words_dict.update(line.split())
    top5_words_list = words_dict.most_common(5)
    return top5_words_list


def main():
    filename = '/usr/share/doc/ImageMagick-6.7.8.9/README.txt'
    top5_words = generate_dict(filename)
    for i in top5_words:
        print(i[0], ': ', i[1])


if __name__ == '__main__':
    main()
