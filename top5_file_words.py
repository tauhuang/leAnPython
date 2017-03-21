#!/usr/bin/python
# -*-  coding: UTF-8 -*-
# counts of each word in file, print the words which counts is top 5.
# use common dict


from __future__ import print_function
import heapq


def generate_dict(filename):
    word_count = {}
    with open(filename) as f:
        for line in f:
            for word in line.split():
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count


def generate_dict_pretty(filename):
    word_count = {}
    with open(filename) as f:
        for line in f:
            for word in line.split():
                word_count.update({word: (word_count.get(word, 0)+1)})
    return word_count


def counts_dict(word_dict):
    counts = word_dict.itervalues()
    largest5 = heapq.nlargest(5, counts)
    print(largest5)
    for i in word_dict:
        if word_dict[i] in largest5:
            print(i, word_dict[i])


def main():
    # filename = input('inpurt filename(fullpath):')
    filename = '/usr/share/doc/ImageMagick-6.7.8.9/README.txt'
    # word_dict = generate_dict(filename)
    word_dict = generate_dict_pretty(filename)
    counts_dict(word_dict)


if __name__ == '__main__':
    main()
