#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# nuannuan.py - Autobot for Nikki UP2U - World Traveller New 2
#
# Copyright (C) 2014 Haoliang Wang
#
# 09/09/2014
#

from random import random
from config import *
from user import *
from utils import *

# Main Function
if __name__ == '__main__':

	log_init()

	task_list = [
		{'map_id':3, 'task_id':16,},
		{'map_id':3, 'task_id':19,},
		{'map_id':3, 'task_id':20,},
		{'map_id':3, 'task_id':21,},
		{'map_id':3, 'task_id':135,},
		{'map_id':3, 'task_id':24,},
		{'map_id':3, 'task_id':26,},
		{'map_id':3, 'task_id':27,},
		{'map_id':3, 'task_id':32,},
		{'map_id':3, 'task_id':33,},
	]

	'''
	task_list = [
		{'map_id':105, 'task_id':1017,},
		{'map_id':105, 'task_id':1018,},
		{'map_id':105, 'task_id':1019,},
		{'map_id':105, 'task_id':1020,},
		{'map_id':105, 'task_id':1021,},
		{'map_id':105, 'task_id':1022,},
	]
	'''

	user = User()
	user.update_user()
	user.show_user()

	user.repeat_task(task_list, 10, 10)
	user.repeat_task(task_list[-1:], 10)

	user.play_lottery(2, 49, repeat=True)
	user.sweep_backpack()

	#cl = [10155,11222,11110,11569,10403,11283,10287,11138,10201,10103,10391,11675]
	#save_clothes([get_cloth_info(i) for i in cl], "test_save")

	#user.find_best_cloth(task_list)
