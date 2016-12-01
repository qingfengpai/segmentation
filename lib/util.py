# -*- coding: utf-8 -*-
__author__ = 'qingfengsheng'

import os
import json

# 读取文件
def read_file(path):
	if not os.path.isfile(path):
		raise UserWarning("file donot exist")
		return False
	f = open(path, 'r')
	lines = f.readlines()
	f.close()
	return lines
# end

def check_path(path):
	""" 检查路径是否存在。makedirs: 包含子文件夹 """
	if not os.path.exists(path):
		os.makedirs(path)
# end check_path

def output_v1(path, name, text):
	""" 输出 response 内容到文件 """
	check_path(path)
	file = str(path) + '/' + str(name)
	f = open(file, 'w')
	f.write(text)
	f.close()
# end output