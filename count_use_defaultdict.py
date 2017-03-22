#!/usr/bin/python
# -*- coding: UTF-8 -*-


from __future__ import print_function
from collections import defaultdict
import heapq


def generate_dict(filename):
    word_dict = defaultdict(int)
    with open(filename) as f:
        for line in f:
            for word in line.split():
                word_dict[word] += 1
    return word_dict


def top5_words(word_dict):
    counts = word_dict.values()
    largest5 = heapq.nlargest(5, counts)
    for i in word_dict:
        if word_dict[i] in largest5:
            print(i, word_dict[i])


def main():
    #filename = input('input filename(fullpath):\n')
    filename = '/usr/share/doc/ImageMagick-6.7.8.9/README.txt'
    word_dict = generate_dict(filename)
    top5_words(word_dict)


if __name__ == '__main__':
    main()
