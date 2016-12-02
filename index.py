# -*- coding: utf-8 -*-
__author__ = 'qingfengsheng'

import json

from lib.ltp import Ltp
from lib.util import *


def get_word_freq():
	ltp = Ltp()
	data = read_file('data/7.10.txt')
	ltp.load_lexicon('data/dict_profession.txt')
	words_list = ltp.cut_to_word(data, 1)
	word_freq_dict = ltp.get_word_freq(words_list)
	word_freq_dict = sorted(word_freq_dict.iteritems(), key=lambda d:d[1], reverse=True)
	content = json.dumps(word_freq_dict, encoding="utf-8", ensure_ascii=False)
	output_v1('output', '7.10-word-freq.json', content)
# end

def cut_to_word():
	ltp = Ltp()
	data = read_file('data/7.10.txt')
	content = ltp.article_cut_to_words(data, 1)
	output_v1('output', '7.10-cut_to_word.txt', content)

if __name__ == '__main__':
	cut_to_word()
