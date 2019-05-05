from CartRegressionTree import cartTree

if __name__=='__main__':
	train_data=[[1,2,3,4],[5,6,7,8]]
	train_label=[1,2]
	cart=cartTree(train_data,train_label)
	cart.printTree()
	cart.getTrainData()
