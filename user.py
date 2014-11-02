#!/usr/bin/env python
#
# user.py - Autobot for Nikki UP2U World Traveller New 2
#
# Copyright (C) 2014 Haoliang Wang
#
# 09/09/2014
#

from config import *
from base import *
from utils import *

class User(object):

	name = ""
	gold = 0
	jewel = 0
	max_p = 0
	power = 0
	delay = 0

	session_id = ""
	did = ""

	task_dresses = {}
	task_list = []

	backpack = []
	bp_dict = {}

	lottery_info = {}

	def __init__(self):
		pass

	def check_login_state(self):
		pass

	def query_power(self):
		ret = action('power')
		if ret != {}:
			self.power = ret['data']['power']
			self.delay = int(ret['data']['delay'])

	def update_user(self):
		self.query_power()
		ret = action('user')
		if ret != {}:
			data = ret['data']
			self.name, self.max_p = data['name'],  data['maxpower']
			self.gold, self.jewel = data['gold'], data['jewel']

	def show_user(self):
		fmt = em("Name %s Gold %s Jewel %s Power %s/%s")
		msg = fmt % (self.name, self.gold, self.jewel, self.power, self.max_p)
		log.info(msg)
		print msg

	def wait_power(self, power_threshold):
		while True:
			self.query_power()
			demand = power_threshold - self.power + POWER_PER_TASK
			if demand <= 0:
				break
			else:
				msg = "Wait power %d => %d " % (self.power, self.power + demand)
				log.info(msg)
				wait(self.delay + (demand - 1) * POWER_INTERVAL, 0, msg)

	def do_task(self, task_id, map_id):
		dress = task_dresses[map_id][task_id]
		ret = action('task_set', task_id = task_id, map_id = map_id)
		ret = action('task', task_id = task_id, dress = dress)
		if ret != {}:
			data = ret['data']
			fmt = "Map %s Task %s Grade %s Score %d"
			msg = fmt % (map_id, task_id, data['grade'], data['score'])
			log.info(msg)
			print msg

	def repeat_task(self, task_list, power_threshold, loop_count = 0):
		count = 0
		while True:
			self.wait_power(power_threshold)
			task = task_list[count % len(task_list)]
			self.do_task(task['task_id'], task['map_id'])
			count = count + 1
			if count == loop_count:
				break

	def play_lottery(self, lot, count, repeat = False, cnt = 0, th = 15500):
		self.get_backpack()
		new_clothes = []
		n = 0
		while True:
			self.update_user()
			if self.gold > th:
				cnt = cnt - 1
				ret = action('lottery', lot = lot, count = count)
				n += 1
				if ret != {}:
					for item in ret['data']['prize']:
						if item['type'] == 3 and not item['content'] in self.bp_dict:
							print "New item %s obtained" % item['content']
							new_clothes.append(get_cloth_info(item['content']))
				if not repeat or cnt == 0:
					break
			else:
				break
		print "%d Lottery played %d newly obtained items saved" % (n, save_clothes(new_clothes, "Lottery"))

	def get_backpack(self, mtype = 0):
		ret = action('backpack', mtype = mtype)
		if ret != {}:
			self.backpack = ret['data']
			self.bp_dict = {}
			for item in self.backpack:
				self.bp_dict[item['itemid']] = item['quantity']

	def sell_backpack(self, item_id, count, mtype):
		ret = action('sell', mtype = mtype, item_id = item_id, count = count)
		if ret != {}:
			print "Items Id %d Sold %d" % (item_id, count)

	def sweep_backpack(self, mtype = 0):
		self.get_backpack(mtype)
		for item in self.backpack:
			if item['quantity'] > 1:
				self.sell_backpack(item['itemid'], item['quantity'] - 1, mtype)

	def find_best_cloth(self, task_list):
		import sqlite3

		conn = sqlite3.connect('db/Introduction_cracked.db')
		c = conn.cursor()
		tl = []
		self.get_backpack()

		for task in task_list:
			tl.append(task['task_id'])

		for task in tl:
			c.execute('SELECT dress_id FROM T_Grading WHERE task_id=? AND grade="S"', (task,))
			ret = c.fetchall()
			good_clothes = []
			for cloth_id in [int(item[0]) for item in ret]:
				if cloth_id in self.bp_dict:
					good_clothes.append(cloth_id)
			save_clothes([get_cloth_info(i) for i in good_clothes], "Task-"+str(task)+"-")
			
		conn.close()
