#!/usr/bin/env python

import codecs
from collections import namedtuple


Hanzi = namedtuple('Hanzi', 'hanzi freq freq_percent pinyin english')


def parse_pinyin_field(pinyin):
    return set(pinyin.replace('u:', 'v').split('/'))


def parse_english_field(english):
    english_stripped = english.strip()
    if english_stripped:
        return english_stripped.split('/')


def parse_frequency_list(filename):
    freq_f = codecs.open(filename, 'r', encoding='gb2312', errors='replace')

    for line in freq_f:
        if line and line[0].isdigit():
            _, hanzi, freq, freq_percent, pinyin, english = line.split('\t')
            yield Hanzi(
                hanzi, int(freq), float(freq_percent),
                parse_pinyin_field(pinyin), parse_english_field(english),
            )

    freq_f.close()
