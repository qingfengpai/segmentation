# -*- coding: utf-8 -*-
__author__ = 'qingfengsheng'

from pyltp import Segmentor

from lib.lexicon import Lexicon

class Ltp(object):
	"""docstring for Ltp"""
	def __init__(self):
		print 'Ltp:: __init__'
		self.segmentor = Segmentor()
		self.segmentor.load('model/cws.model')
	# end

	def load_lexicon(self, path):
		""" 加载专有名词词典
		@params <String> path 词典列表
		"""
		print 'Ltp:: load_lexicon'
		self.lexicon = Lexicon(path)
	# end

	def cut_to_word(self, data, tab_index=0):
		""" 把文本数据切分成词，返回词列表
		@params <list> file模块读取的数据
		@params <int> 按制表符分割后，需要分词的文本的索引
		@return <list> 词列表
		"""
		print 'Ltp:: cut_to_word'
		content = list()
		for line in data:
			line = line.strip()
			if line == "":
				continue
			text = line.split('\t')
			if len(text) < tab_index + 1:
				continue
			text = text[tab_index]

			proper_noun_list = list()
			if self.lexicon:
				text = self.lexicon.filter(text)

			words_list = self.segmentor.segment(text)
			for word in words_list:
				content.append(word)

		print 'Ltp:: cut_to_word done'
		return content
	# end

	def get_word_freq(self, words_list):
		""" 统计词频
		@params <list> words_list 词列表
		@return <dict> word_freq_dict 词频字典
		"""
		print 'Ltp:: get_word_freq'
		word_freq_dict = dict()
		for word in words_list:
			if not word_freq_dict.has_key(word):
				word_freq_dict[word] = 0
			word_freq_dict[word] += 1
		print 'Ltp:: get_word_freq done'
		return word_freq_dict
	# end


