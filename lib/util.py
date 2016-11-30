# -*- coding: utf-8 -*-
__author__ = 'qingfengsheng'

import os

# 读取文件
def read(path):
	if not os.path.isfile(path):
		raise UserWarning("file donot exist")
		return False
	f = open(path, 'r')
	lines = f.readlines()
	f.close()
	return lines
# end

# 输出文本到文件
def output(path, content):
	f = open(path, 'w')
	f.write(content)
	f.close()
# end
