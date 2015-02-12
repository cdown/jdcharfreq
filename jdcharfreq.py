#!/usr/bin/env python

import codecs
import csv
from collections import namedtuple


fields = ['serial', 'hanzi', 'freq', 'freq_percent', 'pinyin', 'english']
Hanzi = namedtuple('Hanzi', fields)


def parse_pinyin_field(pinyin):
    return set(pinyin.replace('u:', 'v').split('/'))


def parse_english_field(english):
    english_stripped = english.strip()
    if english_stripped:
        return english_stripped.split('/')


def parse_frequency_list(filename):
    freq_f = codecs.open(filename, 'r', encoding='gb2312', errors='replace')
    freq_f_filt = (line for line in freq_f if line and line[0].isdigit())

    for row in csv.DictReader(freq_f_filt, delimiter='\t', fieldnames=fields):
        yield Hanzi(
            int(row['serial']), row['hanzi'], int(row['freq']),
            float(row['freq_percent']), parse_pinyin_field(row['pinyin']),
            parse_english_field(row['english']),
        )

    freq_f.close()
