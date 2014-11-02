#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# htmldoc.py - HTML Generator - Autobot for Nikki UP2U World Traveller New 2
#
# Copyright (C) 2014 Haoliang Wang
#
# 09/09/2014
#

class HTMLDoc(object):

	def __init__(self, s=""):
		self.html = s

	def __add__(self, other):
		return self.set_html(self.html + other.html)

	def __str__(self):
		return self.html.encode('utf-8')

	def set_html(self, s):
		self.html = s
		return self

	def gen_list(self, my_list, type, **kwargs):
		for item in my_list:
			temp = self.html
			self.set_html(item).add(type, **kwargs).set_html(self.html + temp)
		return self

	def add(self, tag, **kwargs):
		options = ""
		for name, value in kwargs.items():
			options = options + ' ' + name + '=' + '"' + str(value) + '"'
		self.html = '<' + tag + options + '>' + self.html + '</' + tag + '>'
		return self

	def add_html(self, **kwargs):
		return self.add('html', **kwargs)

	def add_head(self, **kwargs):
		return self.add('head', **kwargs)

	def add_body(self, **kwargs):
		return self.add('body', **kwargs)

	def add_table(self, **kwargs):
		return self.add('table', **kwargs)

	def add_tr(self, **kwargs):
		return self.add('tr', **kwargs)

	def add_td(self, **kwargs):
		return self.add('td', **kwargs)

	def add_span(self, **kwargs):
		return self.add('span', **kwargs)

	def add_link(self, **kwargs):
		return self.add('link', **kwargs)

	def add_a(self, **kwargs):
		return self.add('a', **kwargs)

	def add_img(self, **kwargs):
		kwargs['src'] = "data:image/jpg;base64," + kwargs['src'].encode('base64')
		return self.add('img', **kwargs)
