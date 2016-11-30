# -*- coding: utf-8 -*-
__author__ = 'qingfengsheng'

from lib import util

class Lexicon(object):
	"""docstring for Lexicon"""
	def __init__(self, path):
		print 'Lexicon:: __init__'
		self.dict = util.read(path)
		print 'Lexicon:: __init__ done'
	# end

	def filter(self, sentence=""):
		"""
		@param <String> sentence
		@return <String> 专有名词 + 过滤掉专有名词后的句子
		"""
		print 'Lexicon:: filter'

		# 专有名词列表
		proper_noun_list = list()

		for line in self.dict:
			word = line.strip()
			if word in sentence:
				proper_noun_list.append(word)
				sentence = sentence.replace(word, ' ')

		print 'Lexicon:: filter done'
		return ' '.join(proper_noun_list) + sentence
	# end
