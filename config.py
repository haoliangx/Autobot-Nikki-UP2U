#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# config.py - Configuration - Autobot for Nikki UP2U World Traveller New 2
#
# Copyright (C) 2014 Haoliang Wang
#
# 09/09/2014
#

# ERROR 40, WARNING 30, INFO 20, DEBUG 10
LOGGING_LEVEL = 20

HTML_DIR = 'html_output'
IMG_WIDTH = 150

# Axz's
session_id = "de9c3481442a11e4befefa163e4a2f07"
session_id = "2cec96254cb111e4b2cbfa163e4a2f07"
session_id = "4aa4d684534d11e4b952fa163e4a2f07"
did = "749b175c43c46c05bb260ace97b3903c72b68334"

# Constant
POST = 1
GET = 0
RETRY_DELAY = 30
RETRY_COUNT = 30
TASK_RAND_DELAY = 10
POWER_PER_TASK = 2
POWER_INTERVAL = 360

base_url = "http://app2.nuan.wan.liebao.cn:51000/"
img_url = "http://image2.nuan.wan.liebao.cn/v1/dress/ipad/%s-1.png"

base_args = {
	"session_id" : session_id,
	"did" : did,
	"client" : "3",
	"client_ver" : "3.3.0",
	"network" : "0",
	"client_os_ver" : "8.0", 
}

my_actions = {
	'user' : {
		'name': 'User Info',
		'method': GET,
		'url': "x/2/user/get",
		'args': {},
	},
	'lottery': {
		'name': 'Lottery Action',
		'method': GET,
		'url': "x/2/lottery/do",
		'args': {"lot": "", "count": "",},
	},
	'power': {
		'name': 'Power Query',
		'method': POST,
		'url': "x/2/user/power/regain",
		'args': {},
	},
	'task': {
		'name': 'Do Task',
		'method': POST,
		'url': "x/2/task/do",
		'args': {"task_id": "","dress": "",},
	},
	'sell': {
		'name': 'Backpack Sell',
		'method': POST,
		'url': "x/2/backpack/sell",
		'args': {'mtype': '0','item_id':'','count':'',},
	},
	'backpack': {
		'name': 'Backpack Check',
		'method': GET,
		'url': "x/2/backpack/get",
		'args': {'mtype': '0','ptype':'0','stype':'0',},
	},
	'task_set': {
		'name': 'Set Task',
		'method': POST,
		'url': "x/2/task/set",
		'args': {'task_id': '','map_id':'',},
	},
	'material_source': {
		'name': 'Material Source',
		'method': GET,
		'url': "x/2/processing/source",
		'args': {'material': '',},
	},
	'processing': {
		'name': 'Processing Design',
		'method': POST,
		'url': "x/2/processing/do",
		'args': {'design_id': '',},
	},
	'processing_get': {
		'name': 'Get Design',
		'method': GET,
		'url': "x/2/processing/user",
		'args': {},
	},
}

task_dresses = {
	3: {
		16: '11014,11380,11203,10083,10189,11406,10201,10956,11338',
		19: '10155,11222,10029,10232,10051,11292,10391',
		20: '10790,11225,10360,10899,11286,11169,10039,10493,11168,10668,10290,10289,11781,11338',
		21: '11617,11619,11624,11628',
		135: '11498,11073,10894,10759,10631,11196,10508,10588,10506,10291,10750,11781,11339',
		24: '10155,11222,11110,11569,10403,11283,10287,11138,10201,10103,10391,11675',
		26: '11027,11388,11561,10759,11427,11001,11002,11634,11783,10291,10668,10290,10289,11781,11338',
		27: '11617,11619,11610,10130,11292,11178,11680,10209,10291,10668,11781,11338',
		32: '11617,11388,11609,10598,11316,10499,11002,10182,10184,10291,10923,11644,11338',
		33: '10089,10023,10426,10051,10080,10037',
	},
	105:{
		1017: '10979,10983,11233,11209,10989,10997,11002,11710,10374,10372,11185,10994,11344',
		1018: '11790,10986,10763,10759,11788,11001,10995,11198,11006,10814,11644,11341',
		1019: '11673,11674,11681,11209,11677,11676,10374,11185,11675',
		1020: '10639,11611,11607,11423,10757,10826,10958,11344',
		1021: '11442,10792,11609,10757,10785,10390,10751,11344',
		1022: '11860,11866,10886,11788,11784,11198,11549,11341',
	},
}

'''
mtype material 40000
ptype present 20000
stype special 30000
clothes 10000
'''