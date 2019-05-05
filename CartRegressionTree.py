import numpy as np
class cartTree:
	def printTree(self):
		print("===================novas================")

	def __init__(self,train_data,train_label):
		self.train_data=train_data
		self.train_label=train_label

	def getTrainData(self):
		print(self.train_data)
		return self.train_data

	def getTrainLabel(self):
		return self.train_label

	def find_best_split(self, train_data, train_label):
		if len(train_data) != len(train_label):
			return False

