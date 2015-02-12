#!/usr/bin/env python

import codecs
from collections import namedtuple


Hanzi = namedtuple(
    'Hanzi',
    ['serial', 'hanzi', 'freq', 'freq_percent', 'pinyin', 'english'],
)


def parse_pinyin_field(pinyin):
    # Some entries with 'v' as the vowel also have 'u:' listed. These should
    # all be unified to 'v'.
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

        serial, hanzi, freq, freq_percent, pinyin, english = line.split('\t')

        serial = int(serial)
        freq = int(freq)
        freq_percent = float(freq_percent)
        pinyin = parse_pinyin_field(pinyin)
        english = parse_english_field(english)

        yield Hanzi(serial, hanzi, freq, freq_percent, pinyin, english)
