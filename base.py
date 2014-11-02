#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# base.py - Network base - Autobot for Nikki UP2U World Traveller New 2
#
# Copyright (C) 2014 Haoliang Wang
#
# 09/09/2014
#

import urllib2
import urllib
import json
import time
import sys
import os
import logging as log
import sqlite3

from config import *
from utils import *
from htmldoc import HTMLDoc

def log_init():
	log.basicConfig(
		stream = sys.stdout, 
		level = LOGGING_LEVEL, 
		format='[%(asctime)s] %(message)s', 
		datefmt='%m/%d %H:%M:%S',
	)

def http_request(spec):

	# Construct parameters
	query_url = base_url + spec['url']
	query_args = urllib.urlencode(
		dict(base_args.items() + spec['args'].items()))

	# Construct request
	if spec['method'] == GET:
		request = urllib2.Request(query_url + '?' + query_args)
	elif spec['method'] == POST:
		request = urllib2.Request(query_url, query_args)
	else:
		request = None

	# Request & Response
	retry_count = 0
	while True:
		try:
			response = urllib2.urlopen(request)
			result = response.read()
			response.close()
			log.debug("HTTP request succeed in %s", em(spec['name']))
			break
		except Exception, e:
			retry_count = retry_count + 1
			if retry_count == RETRY_COUNT:
				log.error("%s Failed. Retry limit reached.", em(spec['name']))
				sys.exit("Exiting...")
			message = "Network Error in %s, wait for retry" % em(spec['name'])
			wait(RETRY_DELAY, 1, message)

	return result

class ReturnError(Exception):

	def __init__(self, code):
		self.code = code

	def __str__(self):
		return repr(self.code)

def action(spec_name, **kwargs):
	my_spec = my_actions[spec_name]
	for name, value in kwargs.items():
		my_spec['args'][name] = value
	try:
		result = json.loads(http_request(my_spec))
		if result['ret'] == 0:
			log.debug("%s succeed with args %s", em(my_spec['name']), kwargs)
			return result
		else:
			raise ReturnError(result['ret'])
	except ReturnError, e:
		e_str = get_err_str(e.code)
		log.error("%s Failed with args %s Code: %d %s", em(my_spec['name']), kwargs, e.code, e_str)
		return {}
	except Exception, e:
		log.error("%s Failed with args %s Unexpected Error %s", em(my_spec['name']), kwargs, e)
		return {}

def get_err_str(err_code):
	conn = sqlite3.connect('db/nuannuan2_v2_cracked.db')
	c = conn.cursor()
	c.execute('SELECT value FROM t_errcode WHERE key=?', (err_code,))
	ret = c.fetchone()
	conn.close()
	if ret == None:
		return "Unexpected error code"
	else:
		return ret[0]

def get_cloth_info(id):
	# Get images
	conn = sqlite3.connect('db/picData_ro_cracked.db')
	c = conn.cursor()
	c.execute('SELECT picBinary FROM picData WHERE name LIKE ?', ('%'+str(id)+'%',))
	ret = c.fetchall()
	conn.close()
	images = []
	for item in ret:
		images.append(str(item[0]))

	# Get info
	conn = sqlite3.connect('db/nuannuan2_cracked.db')
	c = conn.cursor()
	c.execute('SELECT name,level,explain FROM T_Clothes WHERE ID=?', (id,))
	try:
		name, level, explain = c.fetchone()
	except Exception,e:
		name, level, explain = "Unknown", "Unknown", "Unknown"

	conn.close()

	# Return Dict
	return {
		'id': str(id),
		'name': name,
		'level': str(level),
		'explain': explain,
		'images': reversed(images),
	}

def save_clothes(cloth_list, file_name = ""):
	
	if len(cloth_list) == 0:
		return 0

	# Create the header line
	doc = HTMLDoc().gen_list(cloth_list[0].keys(), 'td').add_tr()
	for cloth in cloth_list:
		# Create td for images
		images = HTMLDoc().gen_list([str(HTMLDoc().add_img(width = IMG_WIDTH, src = img)) for img in cloth.pop('images')], 'td')
		id_href = HTMLDoc(cloth['id']).add_a(href = img_url % cloth.pop('id'), target = "_blank").add_td()
		# Create td for other info and create tr
		doc = doc + (id_href + HTMLDoc().gen_list(cloth.values(), 'td') + images).add_tr()
	# Add CSS and body, html tags
	doc = (HTMLDoc("").add_link(rel="stylesheet", href="table_style.css").add_head() + doc.add_table().add_body()).add_html()

	# Test the folder
	if not os.path.exists(HTML_DIR):
		os.makedirs(HTML_DIR)

	# Write to file
	file_name = file_name + '-' + time.strftime('%m-%d-%H_%M_%S') + '.html'
	f = open(os.path.join(HTML_DIR, file_name), "w")
	f.write(str(doc))
	f.close()

	return len(cloth_list)