#This file will only be needed to run
import pandas as pd
import numpy as numpy
from datetime import date
import os

class box:
	def __init__():
		self.task_done = ""
		self.no_of_day = (datetime.date.today() - date(1997, 8, 21)).days()
		self.dest = ""
		self.wake_up = "" #should change in future
		self.sleep = ""
		self.social_media_time = 0
		self.self_time = ""
		self.breakfast = False
		self.food_type = False
		self.GRE_quant = False
		self.GRE_quant_count = 0
		self.GRE_verbal = False
		self.GRE_verbal_count = 0
		self.ML = False
		self.articles_read = 0
		self.words_learned = 0
		self.anger = False
		self.exercise = False
		self.sad_day = False
		self.happy_day = False
		self.got_love = False
		self.pain = False

	def log():
		print("Enter your daily achievement: ")
		self.task_done = str(input())
		print("Did you go anywhere? (Leave blank if nowhere) :")
		self.dest = str(input())
		print("What time did you wake up? : ")
		self.wake_up = str(input())
		print("What time did you go to sleep? : ")
		self.sleep = str(input())
		print("How many hours on social media did you spend?")
		self.social_media_time = float(input())
		print("How many hours for self time did you take out?")
		self.self_time = float(input())
		
		#Health
		print("Did you have breakfast? :")
		self.breakfast = _conv_bool(input())
		print("Did I eat sufficiently? :")
		self.food_type = _conv_bool(input())

		#Studies
		print("Did you study Machine Learning? :")
		self.ML = _conv_bool(input())

		#GREStudies
		print("Did you study GRE_quant today? :")
		self.GRE_quant = _conv_bool(input())
		self.GRE_quant_count = _get_GRE(GRE_quant)
		print("Did you study GRE verbal today? :")
		self.GRE_verbal = _conv_bool(input())
		self.GRE_verbal_count = _get_GRE(GRE_verbal)

		print("How many articles did you read today? :")
		self.articles_read = int(input())
		print("How many words did you learn today? :")
		self.words_learned = int(input())

		#Day Review
		print("Did you feel anger today? :")
		self.anger = _conv_bool(input())
		print("Did you feel sad today? :")
		self.sad_day = _conv_bool(input())
		print("Were you happy today? :")
		self.happy_day = _conv_bool(input())
		print("Did someone love you today? :")
		self.got_love = _conv_bool(input())
		print("Did you exercise today? :")
		self.exercise = _conv_bool(input())
		print("Was your body in pain? :")
		self.pain = _conv_bool(input())

	def _get_GRE(self, ip):
		if self._conv_bool(ip):
			print("How many questions did you solve?")
			return int(input())
		else: 
			return 0

	def _conv_bool(self, x):
		if ('Y' or 'y' or True):
			return True
		else : 
			return False


if __name__ == '__main__':
	import os
	print(os.getcwd())