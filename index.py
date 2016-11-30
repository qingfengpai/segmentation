# -*- coding: utf-8 -*-
__author__ = 'qingfengsheng'

import json

from pyltp import Segmentor

from lib.ltp import Ltp
from lib.util import *


if __name__ == '__main__':
	ltp = Ltp()
	data = read('data/7.10.txt')
	ltp.load_lexicon('data/dict_profession.txt')
	words_list = ltp.cut_to_word(data, 1)
	word_freq_dict = ltp.get_word_freq(words_list)
	word_freq_dict = sorted(word_freq_dict.iteritems(), key=lambda d:d[1], reverse=True)
	content = json.dumps(word_freq_dict, encoding="utf-8", ensure_ascii=False)
	output('output/7.10-word-freq.txt', content)

