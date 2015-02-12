#!/usr/bin/env python

import codecs
from collections import namedtuple


Hanzi = namedtuple('Hanzi', 'hanzi freq freq_percent pinyin english')


def parse_pinyin_field(pinyin):
    pinyin = pinyin.replace('u:', 'v')
    pinyin = pinyin.split('/')
    return set(pinyin)


def parse_english_field(english):
    english = english.strip()

    if not english:
        return None
    else:
        return english.split('/')


def parse_frequency_list(filename):
    freq_f = codecs.open(filename, 'r', encoding='gb2312', errors='replace')

    for line in freq_f:
        if not line or not line[0].isdigit():
            continue

        _, hanzi, freq, freq_percent, pinyin, english = line.split('\t')

        pinyin = parse_pinyin_field(pinyin)
        english = parse_english_field(english)

        yield Hanzi(hanzi, int(freq), float(freq_percent), pinyin, english)
