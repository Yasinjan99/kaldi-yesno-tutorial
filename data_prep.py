#! /usr/bin/env python

import os
import os.path
import sys

zeroes = []
ones = []
for fn in os.listdir('waves_yesno'):
    if fn.startswith('0'):
        zeroes.append(fn)  # => training set
    elif fn.startswith('1'):
        ones.append(fn)  # => test set


def text(filenames):
    results = []
    for filename in filenames:
        basename = filename.split('.')[0]
        transcript = basename.replace('1', 'YES').replace('0', 'NO').replace('_', " ")
        results.append("{} {}".format(basename, transcript))

    return '\n'.join(sorted(results))


with open('data/train_yesno/text', 'w') as train_text, open('data/test_yesno/text', 'w') as test_text:
    train_text.write(text(zeroes))
    test_text.write(text(ones))


def wav_scp(filenames):
    results = []
    for filename in filenames:
        basename = filename.split('.')[0]
        wav_path = 'waves_yesno/' + basename + '.wav'
        results.append("{} {}".format(basename, wav_path))

    return '\n'.join(sorted(results))


with open('data/train_yesno/wav.scp', 'w') as train_text, open('data/test_yesno/wav.scp', 'w') as test_text:
    train_text.write(wav_scp(zeroes))
    test_text.write(wav_scp(ones))


def utt2spk(filenames):
    results = []
    for filename in filenames:
        basename = filename.split('.')[0]
        spk = 'global'
        results.append("{} {}".format(basename, spk))

    return '\n'.join(sorted(results))


with open('data/train_yesno/utt2spk', 'w') as train_text, open('data/test_yesno/utt2spk', 'w') as test_text:
    train_text.write(utt2spk(zeroes))
    test_text.write(utt2spk(ones))


def spk2utt(filenames):
    results = []
    for filename in filenames:
        basename = filename.split('.')[0]
        results.append("{} ".format(basename))

    return 'global ' + ''.join(sorted(results))


with open('data/train_yesno/spk2utt', 'w') as train_text, open('data/test_yesno/spk2utt', 'w') as test_text:
    train_text.write(spk2utt(zeroes))
    test_text.write(spk2utt(ones))
